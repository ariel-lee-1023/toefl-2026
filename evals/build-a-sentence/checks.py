#!/usr/bin/env python3
"""Behavioral invariants of the mechanical validator, independent of coaching prose."""
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('validator', ROOT / 'scripts/validate-build-a-sentence.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)
ITEMS = json.loads((HERE / 'items.json').read_text())
KEYS = json.loads((HERE / 'keys.json').read_text())


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.item = deepcopy(ITEMS[0])
        self.key = deepcopy(KEYS[0])
        self.attempt = {'slots': dict(self.key['accepted'][0]['slots'])}

    def reject(self, attempt, fragment):
        with self.assertRaisesRegex(v.Invalid, fragment):
            v.check_arrangement(self.item, attempt)

    def test_all_reviewed_keys_reconstruct(self):
        for item, key in zip(ITEMS, KEYS):
            with self.subTest(item=item['id']):
                for arrangement in key['accepted']:
                    self.assertEqual(v.grade_attempt(item, key, arrangement)['outcome'], 'accepted')
                    result = v.check_arrangement(item, arrangement)
                    self.assertEqual(result['answer'], arrangement['answer'])
                    self.assertEqual(len(arrangement['slots']) + len(result['unused']), len(item['tiles']))

    def test_multiword_intact(self):
        result = v.check_arrangement(self.item, self.attempt)
        self.assertEqual(result['answer'], 'Do you know whether the library is open?')
        self.attempt['slots']['s2'] = 'the'
        self.reject(self.attempt, 'unknown tile')

    def test_repeated_identical_instances_equivalent(self):
        item, key = ITEMS[9], KEYS[9]
        attempt = {'slots': dict(key['accepted'][0]['slots'])}
        attempt['slots']['s1'], attempt['slots']['s3'] = attempt['slots']['s3'], attempt['slots']['s1']
        self.assertEqual(v.grade_attempt(item, key, attempt)['outcome'], 'accepted')
        attempt['slots']['s3'] = attempt['slots']['s1']
        with self.assertRaisesRegex(v.Invalid, 'reused'):
            v.grade_attempt(item, key, attempt)

    def test_missing_slot(self):
        del self.attempt['slots']['s1']
        self.reject(self.attempt, 'slot references')

    def test_unknown_slot(self):
        self.attempt['slots']['s99'] = self.attempt['slots'].pop('s1')
        self.reject(self.attempt, 'slot references')

    def test_reused_tile(self):
        self.attempt['slots']['s2'] = self.attempt['slots']['s1']
        self.reject(self.attempt, 'reused')

    def test_unknown_tile(self):
        self.attempt['slots']['s1'] = 'absent'
        self.reject(self.attempt, 'unknown tile')

    def test_unused_complete_and_unique(self):
        self.attempt['unused'] = []
        self.reject(self.attempt, 'accounting mismatch')
        self.attempt['unused'] = ['t5', 't5']
        self.reject(self.attempt, 'duplicates')
        self.attempt['unused'] = ['missing']
        self.reject(self.attempt, 'accounting mismatch')

    def test_frame_move_and_punctuation_edits(self):
        for text in ('Whether the library is open do you know?',
                     'Do you know whether the library is open.',
                     'Do you know whether the library was open?',
                     'do you know whether the library is open?'):
            with self.subTest(text=text):
                self.attempt['answer'] = text
                self.reject(self.attempt, 'does not reconstruct')

    def test_frame_override_rejected(self):
        self.attempt['frame'] = [{'text': 'A different sentence.'}]
        self.reject(self.attempt, 'immutable item')

    def test_whitespace_only_normalization(self):
        self.attempt['answer'] = '  Do you know whether the  library is open?\n'
        self.assertTrue(v.check_arrangement(self.item, self.attempt)['mechanically_valid'])

    def test_documented_key_answer_must_reconstruct(self):
        self.key['accepted'][0]['answer'] = 'Do you know whether the library was open?'
        with self.assertRaisesRegex(v.Invalid, 'does not reconstruct'):
            v.validate_key(self.item, self.key)

    def test_duplicate_schema_ids(self):
        for kind in ('tile', 'slot'):
            item = deepcopy(self.item)
            if kind == 'tile':
                item['tiles'].append(item['tiles'][0])
            else:
                item['frame'].append({'slot': 's1'})
            with self.subTest(kind=kind), self.assertRaisesRegex(v.Invalid, 'duplicate'):
                v.validate_item(item)

    def test_malformed_shapes_fail_clearly(self):
        for value in (None, [], 'bad', 17):
            with self.subTest(value=value), self.assertRaises(v.Invalid):
                v.validate_item(value)
        for field, value in [('frame', [None]), ('tiles', [{}]), ('provenance', []), ('schema_version', True)]:
            item = deepcopy(self.item)
            item[field] = value
            with self.subTest(field=field), self.assertRaises(v.Invalid):
                v.validate_item(item)

    def test_alternative_and_unknown_arrangements(self):
        item, key = ITEMS[10], KEYS[10]
        for accepted in key['accepted']:
            self.assertEqual(v.grade_attempt(item, key, accepted)['outcome'], 'accepted')
        # Accounting is valid even when the embedded clause has the wrong order.
        self.attempt['slots']['s2'], self.attempt['slots']['s3'] = self.attempt['slots']['s3'], self.attempt['slots']['s2']
        result = v.grade_attempt(self.item, self.key, self.attempt)
        self.assertTrue(result['mechanically_valid'])
        self.assertEqual(result['outcome'], 'unresolved')

    def test_unreviewed_or_flawed_match_not_promoted(self):
        for status in ('draft', 'flawed'):
            self.item['review_status'] = status
            self.assertEqual(v.grade_attempt(self.item, self.key, self.attempt)['outcome'], 'unresolved')

    def test_json_duplicate_property_rejected(self):
        with self.assertRaisesRegex(v.Invalid, 'duplicate JSON property'):
            json.loads('{"s1":"t1","s1":"t2"}', object_pairs_hook=v.object_pairs)

    def test_cli_success_and_constraint_failure(self):
        command = [sys.executable, str(ROOT / 'scripts/validate-build-a-sentence.py')]
        result = subprocess.run(command + [str(HERE / 'items.json'), '--keys', str(HERE / 'keys.json')], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            (folder/'item.json').write_text(json.dumps(self.item))
            self.attempt['slots']['s1'] = 'missing'
            (folder/'attempt.json').write_text(json.dumps(self.attempt))
            result = subprocess.run(command + [str(folder/'item.json'), '--attempt', str(folder/'attempt.json')], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn('unknown tile', json.loads(result.stderr)['error'])
            (folder/'item.json').write_text('{broken')
            result = subprocess.run(command + [str(folder/'item.json')], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn('error', json.loads(result.stderr))


if __name__ == '__main__':
    unittest.main(verbosity=2)
