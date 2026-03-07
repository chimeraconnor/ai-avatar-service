#!/usr/bin/env python3
import json
import random
from collections import Counter

def generate_human_labels(data):
    """Generate 2-4 word human-readable labels for each cluster."""

    # Build vocabulary from chunk titles and content
    vocab = {}
    for node in data['nodes']:
        cluster_id = node.get('cluster_id')
        if cluster_id is None:
            continue

        if cluster_id not in vocab:
            vocab[cluster_id] = []

        # Add words from title
        title = node.get('title', '').lower()
        words = [w.strip('.,!?;:"()[]{}') for w in title.split() if len(w) > 2]
        vocab[cluster_id].extend(words)

        # Add words from content (sample first 200 chars)
        content = node.get('content', '').lower()[:200]
        words = [w.strip('.,!?;:"()[]{}') for w in content.split() if len(w) > 3]
        vocab[cluster_id].extend(words)

    # Generate labels for each cluster
    labels = {}
    for cluster in data['clusters']:
        cluster_id = cluster['id']

        if cluster_id not in vocab or not vocab[cluster_id]:
            labels[cluster_id] = "unlabeled cluster"
            continue

        # Count word frequency
        word_counts = Counter(vocab[cluster_id])

        # Filter out common/meaningless words
        stop_words = {
            'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can', 'her',
            'was', 'one', 'our', 'out', 'who', 'this', 'that', 'with', 'they',
            'have', 'from', 'been', 'more', 'when', 'will', 'would', 'there',
            'their', 'what', 'about', 'which', 'like', 'than', 'then', 'them',
            'also', 'into', 'some', 'could', 'just', 'over', 'such', 'your',
            'only', 'these', 'very', 'time', 'work', 'make', 'need', 'things',
            'just', 'should', 'really', 'first', 'since', 'must', 'going',
            'still', 'being', 'while', 'after', 'might', 'before', 'through'
        }

        filtered = {w: c for w, c in word_counts.items() if w not in stop_words and c > 1}

        if not filtered:
            # Fallback to most frequent non-stop words
            filtered = {w: c for w, c in word_counts.items() if w not in stop_words}

        if not filtered:
            labels[cluster_id] = f"cluster {cluster_id}"
            continue

        # Get top 3-4 words
        top_words = [w for w, _ in sorted(filtered.items(), key=lambda x: x[1], reverse=True)[:4]]

        # Clean up words
        cleaned_words = []
        for word in top_words:
            # Remove common suffixes
            if word.endswith('ing'):
                word = word[:-3]
            elif word.endswith('ed'):
                word = word[:-2]
            elif word.endswith('ly'):
                word = word[:-2]
            elif word.endswith('s') and len(word) > 4:
                word = word[:-1]

            if len(word) >= 3:
                cleaned_words.append(word)

        # Create label
        if len(cleaned_words) >= 2:
            label = ' / '.join(cleaned_words[:4])
        elif len(cleaned_words) == 1:
            label = cleaned_words[0]
        else:
            label = f"cluster {cluster_id}"

        # Ensure 2-4 words
        label_parts = label.split(' / ')
        if len(label_parts) > 4:
            label = ' / '.join(label_parts[:4])

        labels[cluster_id] = label

    return labels

if __name__ == '__main__':
    # Load graph data
    with open('graph_data.json', 'r') as f:
        data = json.load(f)

    print(f"Generating labels for {len(data['clusters'])} clusters...")

    # Generate labels
    labels = generate_human_labels(data)

    # Update clusters with new labels
    for cluster in data['clusters']:
        cluster_id = cluster['id']
        if cluster_id in labels:
            old_label = cluster['label']
            new_label = labels[cluster_id]
            if old_label != new_label:
                print(f"  Cluster {cluster_id}: '{old_label}' -> '{new_label}'")
            cluster['label'] = new_label

    # Save updated data
    with open('graph_data.json', 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\nDone! Updated graph_data.json with human-readable labels.")
