#!/bin/bash
# TTS wrapper script for Kokoro v1.0
# Usage: tts-speak.sh "Text to speak" [output_file] [model_type] [speaker_id]

TEXT="${1:-"Hello, world"}"
OUTPUT="${2:-/tmp/tts-output.wav}"
MODEL_TYPE="${3:-kokoro}"
SPEAKER_ID="${4:-6}"  # Default: af_nicole (6), af_bella (1)

# Paths
BINARY="/home/node/.openclaw/workspace/tools/sherpa-onnx-tts/runtime/bin/sherpa-onnx-offline-tts"
MODEL="/home/node/.openclaw/workspace/.kokoro-v1.0/model.onnx"
TOKENS="/home/node/.openclaw/workspace/.kokoro-v1.0/tokens.txt"
VOICES="/home/node/.openclaw/workspace/.kokoro-v1.0/voices.bin"
DATA_DIR="/home/node/.openclaw/workspace/.kokoro-v1.0/espeak-ng-data"

# Check if binary exists
if [ ! -f "$BINARY" ]; then
    echo "Error: Kokoro binary not found at $BINARY"
    exit 1
fi

# Run TTS
"$BINARY" \
    --kokoro-model="$MODEL" \
    --kokoro-tokens="$TOKENS" \
    --kokoro-voices="$VOICES" \
    --kokoro-data-dir="$DATA_DIR" \
    --kokoro-lang="en" \
    --sid="$SPEAKER_ID" \
    --output-filename="$OUTPUT" \
    "$TEXT"
