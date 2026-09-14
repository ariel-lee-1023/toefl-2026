#!/usr/bin/env python3
"""Render original plain-text listening scripts with installed macOS voices."""

import argparse
import array
import hashlib
import json
import platform
import re
import shutil
import subprocess
import tempfile
import wave
from pathlib import Path


def run(args):
    return subprocess.run(args, check=True, capture_output=True, text=True, timeout=120)


def capabilities():
    say, convert = shutil.which("say"), shutil.which("afconvert")
    if platform.system() != "Darwin" or not say or not convert:
        raise ValueError("Audio unavailable: requires macOS with say and afconvert.")
    voices = {}
    for line in run([say, "-v", "?"]).stdout.splitlines():
        match = re.match(r"^(.*?)\s+(en_[A-Za-z_]+)\s+#", line)
        if match:
            voices[match[1].strip()] = match[2]
    if not voices:
        raise ValueError("Audio unavailable: no installed English voices were reported.")
    return say, convert, voices


def validate(data, voices):
    rate = data.get("rate", 155)
    if not isinstance(rate, int) or isinstance(rate, bool) or not 80 <= rate <= 220:
        raise ValueError("rate must be an integer from 80 to 220 words per minute.")
    segments = data.get("segments")
    if not isinstance(segments, list) or not 1 <= len(segments) <= 40:
        raise ValueError("Provide 1 to 40 speech segments.")
    speaker_voices, used_voices = {}, {}
    for segment in segments:
        if not isinstance(segment, dict):
            raise ValueError("Each segment must be an object.")
        speaker, voice, text = (segment.get(k) for k in ("speaker", "voice", "text"))
        if not all(isinstance(v, str) and v.strip() for v in (speaker, voice, text)):
            raise ValueError("Every segment needs nonempty speaker, voice, and text strings.")
        if voice not in voices:
            raise ValueError(f"Unavailable English voice: {voice}. Run --probe to list voices.")
        if speaker in speaker_voices and speaker_voices[speaker] != voice:
            raise ValueError("Keep a speaker's voice consistent.")
        if voice in used_voices and used_voices[voice] != speaker:
            raise ValueError("Use distinct voices for distinct speaker roles.")
        speaker_voices[speaker], used_voices[voice] = voice, speaker
        if "[[" in text or "]]" in text or any(ord(c) < 32 and c not in "\n\t" for c in text):
            raise ValueError("Use plain speech text without renderer markup or control characters.")
        if len(text.split()) > 400:
            raise ValueError("A segment exceeds this short-practice adapter's 400-word limit.")
    return rate, segments


def render(source, output):
    say, convert, voices = capabilities()
    raw = source.read_bytes()
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("The script must be a JSON object.")
    rate, segments = validate(data, voices)
    if output.exists():
        raise ValueError("Output already exists; choose a fresh directory to preserve prior work.")
    output.parent.mkdir(parents=True, exist_ok=True)
    # Build privately, then publish the complete directory only after all segments pass.
    with tempfile.TemporaryDirectory(prefix=".listening-", dir=output.parent) as temporary:
        work = Path(temporary)
        result = work / "result"
        result.mkdir()
        audio_path = result / "audio.wav"
        manifest_segments = []
        with wave.open(str(audio_path), "wb") as audio:
            audio.setparams((1, 2, 16000, 0, "NONE", "not compressed"))
            for index, segment in enumerate(segments):
                text_file, aiff_file, wav_file = (work / f"segment-{index}.{ext}" for ext in ("txt", "aiff", "wav"))
                text_file.write_text(segment["text"], encoding="utf-8")
                run([say, "-v", segment["voice"], "-r", str(rate), "-f", str(text_file), "-o", str(aiff_file)])
                run([convert, "-f", "WAVE", "-d", "LEI16@16000", "-c", "1", str(aiff_file), str(wav_file)])
                with wave.open(str(wav_file), "rb") as rendered:
                    if (rendered.getnchannels(), rendered.getsampwidth(), rendered.getframerate()) != (1, 2, 16000):
                        raise ValueError("Unexpected rendered PCM format.")
                    frames = rendered.readframes(rendered.getnframes())
                samples = array.array("h", frames)
                if len(samples) < 1600 or max(abs(v) for v in samples) < 100:
                    raise ValueError("Rendering produced empty, very short, or silent audio.")
                if index:
                    audio.writeframes(b"\0\0" * 4000)
                audio.writeframes(frames)
                manifest_segments.append({
                    "speaker": segment["speaker"], "voice": segment["voice"],
                    "text_sha256": hashlib.sha256(segment["text"].encode()).hexdigest(),
                    "seconds": round(len(samples) / 16000, 3),
                })
        with wave.open(str(audio_path), "rb") as audio:
            duration = audio.getnframes() / audio.getframerate()
        manifest = {
            "provenance": "Original practice; local macOS speech synthesis, not ETS audio",
            "source_sha256": hashlib.sha256(raw).hexdigest(),
            "audio_sha256": hashlib.sha256(audio_path.read_bytes()).hexdigest(),
            "rate": rate, "seconds": round(duration, 3), "segments": manifest_segments,
            "verification": "Input hashes, PCM format, duration, and non-silence checked. Acoustic correspondence requires playback or ASR review.",
        }
        (result / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
        if output.exists():
            raise ValueError("Output appeared during rendering; refusing to overwrite it.")
        result.rename(output)
    return {"audio": str(output / "audio.wav"), "manifest": str(output / "manifest.json"), "seconds": manifest["seconds"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", type=Path)
    parser.add_argument("output", nargs="?", type=Path)
    parser.add_argument("--probe", action="store_true")
    args = parser.parse_args()
    try:
        if args.probe:
            _, _, voices = capabilities()
            print(json.dumps({"adapter": "macOS say", "voices": voices, "playable_format": "WAV", "acoustic_review": "external"}, indent=2))
        elif args.source and args.output:
            print(json.dumps(render(args.source.resolve(), args.output.resolve()), indent=2))
        else:
            parser.error("provide source.json and a new output directory, or --probe")
    except (ValueError, OSError, subprocess.SubprocessError) as error:
        # Do not leak the private script or renderer output into a blind exercise.
        if isinstance(error, subprocess.SubprocessError):
            parser.exit(1, "Audio rendering failed; inspect host capability and retry, or use the labelled text-only fallback.\n")
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
