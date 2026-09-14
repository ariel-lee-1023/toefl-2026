#!/usr/bin/env python3
"""Deterministic checks complementing recorded behavioral forward tests."""

import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import tempfile
import unittest
import wave
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXAMPLES = Path(__file__).parent / "examples"
spec = importlib.util.spec_from_file_location("audio_adapter", ROOT / "scripts/render-listening.py")
adapter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(adapter)


class PracticeChecks(unittest.TestCase):
    def test_complete_words_round_trip(self):
        data = json.loads((EXAMPLES / "complete-words.json").read_text())
        original = " ".join(data[k] for k in ("first_sentence", "middle", "last"))
        self.assertTrue(70 <= len(original.split()) <= 100)
        self.assertEqual(len(data["key"]), 10)
        self.assertEqual([k["position_after_first_sentence"] for k in data["key"]], list(range(2, 21, 2)))
        masks = re.findall(r"([A-Za-z]+)(_+)", data["masked"])
        self.assertEqual(len(masks), 10)
        restored = data["masked"]
        for (prefix, blanks), key in zip(masks, data["key"]):
            self.assertEqual(prefix, key["prefix"])
            self.assertEqual(len(blanks), key["missing"])
            self.assertEqual(prefix + key["suffix"], key["word"])
            self.assertEqual(len(prefix), len(key["word"]) // 2)
            restored = restored.replace(prefix + blanks, key["word"], 1)
        self.assertEqual(restored, original)

    def test_audio_fixture_integrity(self):
        directory = EXAMPLES / "announcement-audio"
        manifest = json.loads((directory / "manifest.json").read_text())
        self.assertEqual(hashlib.sha256((EXAMPLES / "announcement-script.json").read_bytes()).hexdigest(), manifest["source_sha256"])
        self.assertEqual(hashlib.sha256((directory / "audio.wav").read_bytes()).hexdigest(), manifest["audio_sha256"])
        with wave.open(str(directory / "audio.wav"), "rb") as audio:
            self.assertEqual((audio.getnchannels(), audio.getsampwidth(), audio.getframerate()), (1, 2, 16000))
            duration = audio.getnframes() / audio.getframerate()
            self.assertTrue(10 < duration < 90)
            self.assertAlmostEqual(duration, manifest["seconds"], places=2)
            self.assertTrue(any(audio.readframes(audio.getnframes())))

    def test_audio_rejects_ambiguous_roles_and_control_markup(self):
        voices = {"Samantha": "en_US", "Daniel": "en_GB"}
        valid = {"segments": [{"speaker": "A", "voice": "Samantha", "text": "The library opens at nine."}]}
        self.assertEqual(adapter.validate(valid, voices)[0], 155)
        for bad in [
            {"segments": [{"speaker": "A", "voice": "Missing", "text": "Hello."}]},
            {"segments": [{"speaker": "A", "voice": "Samantha", "text": "[[slnc 500]]"}]},
            {"segments": valid["segments"] + [{"speaker": "B", "voice": "Samantha", "text": "Tomorrow?"}]},
            {"segments": valid["segments"] + [{"speaker": "A", "voice": "Daniel", "text": "Tomorrow?"}]},
            {"rate": True, "segments": valid["segments"]},
        ]:
            with self.subTest(input=bad), self.assertRaises(ValueError):
                adapter.validate(bad, voices)

    def test_new_reference_links_resolve(self):
        files = [ROOT / "SKILL.md", ROOT / "README.md", *ROOT.glob("references/*.md"), *ROOT.glob("practice-records/*.md")]
        for path in files:
            text = re.sub(r"```.*?```", "", path.read_text(), flags=re.S)
            text = re.sub(r"`[^`]*`", "", text)
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
                if "://" in target or target.startswith(("#", "mailto:")):
                    continue
                dest = (path.parent / target.split("#", 1)[0]).resolve()
                with self.subTest(file=str(path.relative_to(ROOT)), target=target):
                    self.assertTrue(dest.exists(), f"Missing internal link: {target}")

    def test_archive_input_round_trip(self):
        node = shutil.which("node")
        if not node:
            self.skipTest("Node is needed for unchanged archive scripts")
        with tempfile.TemporaryDirectory(prefix="toefl-archive-check-") as temporary:
            root = Path(temporary)
            scripts = root / ".github/scripts"
            scripts.mkdir(parents=True)
            for name in ("archive-incoming.js", "archive-semantic-consolidation-buffer.js"):
                shutil.copy2(ROOT / ".github/scripts" / name, scripts / name)
            cases = {
                "write-an-email": {"Title": "Email Round Trip", "Prompt": "Ask about enrollment.", "My Polished Response": "Dear Professor, I would like to join your seminar. Best, Alex", "My Score Explained": "Text model assessment."},
                "academic-discussion": {"Title": "Discussion Round Trip", "Prompt": "Maya supports loans. Leo worries about cost.", "My Polished Response": "I support a small trial because actual demand can guide later purchases.", "My Score Explained": "The model addresses the debate with a concrete proposal."},
                "interview": {"Title": "Reading Habits", **{f"Q{i} Prompt": f"Reading question {i}?" for i in range(1, 5)}, **{f"Q{i} My Polished Response": f"Distinct model answer {i}." for i in range(1, 5)}, "My Score Explained": "Model text only; delivery unassessed."},
                "listen-and-repeat": {"Title": "Entrance Instructions", "Prompt": "Please leave your bags beside the entrance.", "Set Map": "action: leave bags; place: beside entrance", "My Chunking & Memory Strategy": "Retain two meaningful chunks.", "My Pronunciation Focus": "Predicted risk: bags plural ending.", "My Self-Assessment": "No attempt; score unavailable."},
            }
            for task, fields in cases.items():
                folder = root / "polished-5-5-responses/incoming" / task
                folder.mkdir(parents=True)
                (folder / "fixture.md").write_text("\n\n".join(f"## {k}\n{v}" for k, v in fields.items()))
            subprocess.run([node, str(scripts / "archive-incoming.js")], check=True, capture_output=True, text=True)
            for task, fields in cases.items():
                outputs = list((root / "polished-5-5-responses" / task).glob("*.md"))
                self.assertEqual(len(outputs), 1)
                rendered = outputs[0].read_text()
                for label, value in fields.items():
                    if label != "Title":
                        self.assertIn(value, rendered)
                self.assertFalse((root / "polished-5-5-responses/incoming" / task / "fixture.md").exists())
            fields = {"Title": "Shade Tree Trial", "TOEFL Domain": "Ecology", "Tier": "T1 (D=3)", "Core Thesis": "Although heat persists, shade trees may improve waiting conditions.", "Pillar A": "Summer heat affects stops.", "Pillar B": "Volunteers water young trees.", "Pillar C": "Future comfort review informs expansion.", "Lexical Bindings": "shade -> solar shelter"}
            incoming = root / "semantic-consolidation-buffer/incoming"
            incoming.mkdir(parents=True)
            (incoming / "fixture.md").write_text("\n\n".join(f"## {k}\n{v}" for k, v in fields.items()))
            subprocess.run([node, str(scripts / "archive-semantic-consolidation-buffer.js")], check=True, capture_output=True, text=True)
            outputs = list((root / "semantic-consolidation-buffer/content").glob("*.md"))
            self.assertEqual(len(outputs), 1)
            rendered = outputs[0].read_text()
            for label, value in fields.items():
                if label != "Title":
                    self.assertIn(value, rendered)


if __name__ == "__main__":
    unittest.main(verbosity=2)
