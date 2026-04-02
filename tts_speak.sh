#!/bin/bash

# TTS wrapper script
# Usage: tts_speak.sh "text" [output_file] [model_type] [speaker_id]
# Example: tts_speak.sh "Hello" output.wav kokoro 1

TEXT="$1"
OUTPUT="${2:-/tmp/tts_output.wav}"
MODEL_TYPE="${3:-kokoro}"
SPEAKER_ID="${4:-1}"

# Path to models (adjust based on your installation)
MODELS_DIR="/home/node/.openclaw/workspace/.kokoro-v1.0"

# Paths to model files
MODEL_FILE="$MODELS_DIR/model.onnx"
TOKENS_FILE="$MODELS_DIR/tokens.txt"

# Check if model files exist
if [ ! -f "$MODEL_FILE" ]; then
    echo "Error: Model file not found: $MODEL_FILE" >&2
    exit 1
fi

if [ ! -f "$TOKENS_FILE" ]; then
    echo "Error: Tokens file not found: $TOKENS_FILE" >&2
    exit 1
fi

# Check if sherpa-onnx binary exists
SHERPA_BIN="/home/node/.openclaw/workspace/tools/sherpa-onnx-tts/runtime/bin/sherpa-onnx-offline-tts"
if [ ! -f "$SHERPA_BIN" ]; then
    echo "Error: sherpa-onnx-offline-tts not found at: $SHERPA_BIN" >&2
    exit 1
fi

# Run TTS
"$SHERPA_BIN" \
    --vits-model="$MODEL_FILE" \
    --vits-tokens="$TOKENS_FILE" \
    --vits-data-dir="$MODELS_DIR/espeak-ng-data" \
    --output-filename="$OUTPUT" \
    --sid="$SPEAKER_ID" \
    --num-threads=4 \
    --debug=false \
    "$TEXT"

# Check if output was created
if [ ! -f "$OUTPUT" ]; then
    echo "Error: Output file not created: $OUTPUT" >&2
    exit 1
fi

echo "Generated: $OUTPUT"
