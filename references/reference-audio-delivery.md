# Audio delivery and supported local adapter

Created 2026-09-14. The skill does not assume a particular speech service or subscription. Discover whether the current host can read supplied audio, generate audio, return a playable artifact, and inspect playback or transcription. These are distinct capabilities. A text transcript proves none of the auditory ones.

## Preferred delivery sequence

1. Use an available host-native audio tool when it can render and return the original script without revealing it to the learner. Follow that tool's actual schema, not an invented audio API.
2. On macOS, use the supported adapter below with locally installed English voices. It requires Python 3 and Apple's built-in `say` and `afconvert`; no account, network request, or paid subscription is needed. Inspect the probe result rather than assuming those voices exist. A sandbox may list voices yet return empty speech output; the adapter rejects that. If the host permits access to its local speech service, retry through its normal permission mechanism; otherwise report audio unavailable and use the fallback.
3. Otherwise offer clearly labelled script-based work or guided practice with an accessible learner-provided recording. State which audio-dependent feature is unavailable. Never present text as a completed listening recording.

Check audio, script, and answer key before delivery. When playback or speech recognition is available, inspect the entire clip for omissions, substitutions, speaker confusion, truncation, and answer-revealing emphasis. If the host cannot inspect spoken content, report that acoustic review remains pending: successful rendering, non-silent PCM, and matching input hashes establish the file pipeline, not what every word sounds like. Reject a clip with known mismatches and regenerate before using its key.

## macOS adapter

From the installed skill folder:

```bash
python3 scripts/render-listening.py --probe
python3 scripts/render-listening.py /absolute/path/private-script.json /absolute/path/practice-audio
```

The output directory must not already exist. The adapter returns only the playable `audio.wav` path and a manifest path in its console result. It does not print the transcript. `manifest.json` stores hashes, voices, duration, and the acoustic-review boundary. The script JSON is a coach-side file, kept out of the learner's first-play response.

```json
{
  "rate": 155,
  "segments": [
    {"speaker": "A", "voice": "Samantha", "text": "Could we meet after class?"},
    {"speaker": "B", "voice": "Daniel", "text": "I have another class then. How about tomorrow?"}
  ]
}
```

Use plain speech text without speaker labels inside the spoken text. The adapter assigns one installed English voice per speaker; different speaker IDs must use different voices. A brief pause separates turns. Rate is an adjustable design choice, not official timing. For a single-speaker announcement or talk, one segment is sufficient. The adapter rejects speech-control markup so that embedded renderer commands cannot silently change pronunciation, insert audio, or omit content.

Attach the WAV through the host's normal audio/file mechanism; in a host supporting Markdown media, use an absolute path: `![Listening practice](/absolute/path/practice-audio/audio.wav)`. Do not link the private script or answer key before the attempt. Playback controls may allow replay, so mark replay-assisted attempts honestly. This adapter does not enforce a test timer, prevent replay, provide ASR, create speaker images, or reproduce an adaptive testing interface.

## Supplied recordings

If the host can access and process the file, use the actual audio and supplied transcript when relevant. Record whether the transcript was supplied or generated, and correct mismatches before grounding questions in it. Use timestamps only when verified from the actual recording or supplied as source metadata, labelled accordingly. If inaccessible, say so and ask for an accessible recording or use the transcript as text-only material. Never infer auditory observations from a transcript.
