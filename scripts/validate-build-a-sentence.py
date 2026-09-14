#!/usr/bin/env python3
"""Check tile accounting, immutable frames and reviewed-key matching, not English."""
import argparse
import json
from pathlib import Path
import sys


class Invalid(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise Invalid(message)


def nonempty(value, label):
    require(isinstance(value, str) and bool(value.strip()), f'{label}: nonempty string required')


def normalize(text):
    return ' '.join(text.split())


def object_pairs(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f'duplicate JSON property: {key}')
        result[key] = value
    return result


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'), object_pairs_hook=object_pairs)


def validate_item(item):
    require(isinstance(item, dict), 'item must be an object')
    require(type(item.get('schema_version')) is int and item['schema_version'] == 1,
            'unsupported schema_version')
    for field in ('id', 'context', 'target_skill', 'estimated_difficulty'):
        nonempty(item.get(field), field)
    require(item.get('review_status') in ('draft', 'reviewed', 'flawed'), 'invalid review_status')
    provenance = item.get('provenance')
    require(isinstance(provenance, dict), 'provenance must be an object')
    require(provenance.get('kind') in ('original', 'adapted', 'supplied', 'official'),
            'invalid provenance kind')
    for field in ('source', 'date'):
        nonempty(provenance.get(field), f'provenance.{field}')
    frame = item.get('frame')
    require(isinstance(frame, list) and frame, 'frame must be a nonempty list')
    slots = []
    for part in frame:
        require(isinstance(part, dict) and (set(part) == {'text'} or set(part) == {'slot'}),
                'frame element must contain exactly text or slot')
        if 'slot' in part:
            nonempty(part['slot'], 'slot ID')
            require(part['slot'] not in slots, f'duplicate slot ID: {part["slot"]}')
            slots.append(part['slot'])
        else:
            require(isinstance(part['text'], str), 'fixed text must be a string')
    require(slots, 'frame must contain a slot')
    tiles = item.get('tiles')
    require(isinstance(tiles, list) and tiles, 'tiles must be a nonempty list')
    bank = {}
    for tile in tiles:
        require(isinstance(tile, dict) and set(tile) == {'id', 'text'}, 'invalid tile object')
        nonempty(tile['id'], 'tile ID')
        nonempty(tile['text'], 'tile text')
        require(tile['id'] not in bank, f'duplicate tile ID: {tile["id"]}')
        bank[tile['id']] = tile['text']
    require(len(bank) >= len(slots), 'not enough tiles to fill frame')
    return slots, bank


def id_set(values, label):
    require(isinstance(values, list), f'{label} must be a list')
    for value in values:
        nonempty(value, label)
    require(len(set(values)) == len(values), f'{label} contains duplicates')
    return set(values)


def check_arrangement(item, arrangement):
    slots, bank = validate_item(item)
    require(isinstance(arrangement, dict), 'arrangement must be an object')
    require(set(arrangement) <= {'slots', 'answer', 'unused', 'expected_unused', 'grammar', 'context_fit'},
            'unknown arrangement fields; frame and tiles belong to the immutable item')
    mapping = arrangement.get('slots')
    require(isinstance(mapping, dict), 'slots must be an object')
    require(set(mapping) == set(slots), 'slot references must fill every required slot exactly once')
    used = list(mapping.values())
    for tile_id in used:
        nonempty(tile_id, 'selected tile ID')
        require(tile_id in bank, f'unknown tile: {tile_id}')
    require(len(set(used)) == len(used), 'tile instance reused')
    unused = [tile_id for tile_id in bank if tile_id not in used]
    for field in ('unused', 'expected_unused'):
        if field in arrangement:
            require(id_set(arrangement[field], field) == set(unused), f'{field} accounting mismatch')
    rendered = normalize(''.join(part['text'] if 'text' in part else bank[mapping[part['slot']]]
                                 for part in item['frame']))
    if 'answer' in arrangement:
        nonempty(arrangement['answer'], 'answer')
        require(normalize(arrangement['answer']) == rendered,
                'answer does not reconstruct from fixed frame and intact selected tiles')
    return {'mechanically_valid': True, 'answer': rendered, 'unused': unused}


def validate_key(item, key):
    validate_item(item)
    require(isinstance(key, dict) and key.get('item_id') == item['id'], 'key item_id mismatch')
    accepted = key.get('accepted')
    require(isinstance(accepted, list) and accepted, 'key needs at least one accepted arrangement')
    review = key.get('review')
    require(isinstance(review, dict), 'key review must be an object')
    for field in ('reviewer', 'date', 'grammar', 'context', 'uniqueness'):
        nonempty(review.get(field), f'review.{field}')
    results = []
    for entry in accepted:
        require(isinstance(entry, dict), 'accepted arrangement must be an object')
        for field in ('answer', 'grammar', 'context_fit'):
            nonempty(entry.get(field), f'accepted.{field}')
        results.append(check_arrangement(item, entry))
    return results


def grade_attempt(item, key, attempt):
    validate_key(item, key)
    result = check_arrangement(item, attempt)
    slots, bank = validate_item(item)
    signature = tuple(bank[attempt['slots'][slot]] for slot in slots)
    matched = any(signature == tuple(bank[entry['slots'][slot]] for slot in slots)
                  for entry in key['accepted'])
    # Review status is a human/model assertion; never promote it from mechanics alone.
    result['key_match'] = matched
    result['outcome'] = 'accepted' if matched and item['review_status'] == 'reviewed' else 'unresolved'
    result['scope'] = 'Mechanical check and reviewed-key lookup only; no grammar or score inference.'
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('items')
    parser.add_argument('--keys')
    parser.add_argument('--attempt', help='Requires exactly one item; optional separate key')
    args = parser.parse_args()
    try:
        loaded = read_json(args.items)
        items = loaded if isinstance(loaded, list) else [loaded]
        require(items, 'empty item set')
        for item in items:
            validate_item(item)
        ids = [item['id'] for item in items]
        require(len(set(ids)) == len(ids), 'duplicate item ID')
        keys = {}
        if args.keys:
            loaded = read_json(args.keys)
            entries = loaded if isinstance(loaded, list) else [loaded]
            for key in entries:
                require(isinstance(key, dict), 'key must be an object')
                nonempty(key.get('item_id'), 'key.item_id')
                require(key['item_id'] not in keys, 'duplicate key item_id')
                keys[key['item_id']] = key
            require(set(keys) == set(ids), 'keys must match item IDs exactly')
        if args.attempt:
            require(len(items) == 1, 'attempt mode requires one item')
            item = items[0]
            attempt = read_json(args.attempt)
            result = (grade_attempt(item, keys[item['id']], attempt) if keys
                      else check_arrangement(item, attempt))
        else:
            result = [{'item_id': item['id'], 'structure_valid': True,
                       'accepted_arrangements': validate_key(item, keys[item['id']]) if keys else None}
                      for item in items]
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0
    except (Invalid, OSError, ValueError) as exc:
        print(json.dumps({'error': str(exc)}), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
