#!/usr/bin/env python3
"""
Text preprocessing for TTS to produce natural-sounding speech.
Removes or modifies punctuation and symbols that would be read aloud awkwardly.
"""
import sys
import re

def preprocess_text(text):
    # Remove ellipsis (...) but keep the pause implication
    text = re.sub(r'\.{3,}', ',', text)

    # Handle em-dashes — replace with slight pause
    text = re.sub(r'—', ',', text)

    # Remove asterisks (*emphatic text*)
    text = re.sub(r'\*([^*]+)\*', r'\1', text)

    # Remove underscores (_italic text_)
    text = re.sub(r'_([^_]+)_', r'\1', text)

    # Convert "..." to natural pause marker
    text = re.sub(r'\.\.\.', ', ', text)

    # Handle abbreviations - ensure they're not read letter-by-letter
    # For example: "Mr." → "Mister", "Mrs." → "Missus", etc.
    text = re.sub(r'\bMr\.\s+', 'Mister ', text)
    text = re.sub(r'\bMrs\.\s+', 'Missus ', text)
    text = re.sub(r'\bMs\.\s+', 'Ms ', text)
    text = re.sub(r'\bDr\.\s+', 'Doctor ', text)
    text = re.sub(r'\bProf\.\s+', 'Professor ', text)

    # Handle "well..." type transitions
    text = re.sub(r'\bwell\b\.{0,2}', 'well', text, flags=re.IGNORECASE)

    # Remove multiple spaces
    text = re.sub(r' +', ' ', text)

    # Clean up any double commas from replacements
    text = re.sub(r',,', ',', text)

    # Remove leading/trailing whitespace
    text = text.strip()

    return text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: tts_preprocess.py 'text to preprocess'", file=sys.stderr)
        sys.exit(1)

    text = ' '.join(sys.argv[1:])
    print(preprocess_text(text))
