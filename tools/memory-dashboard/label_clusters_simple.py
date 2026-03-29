#!/usr/bin/env python3
"""
Label clusters with human-readable names based on their node content.
Reads graph_data.json, analyzes cluster content, and updates labels.
"""

import json
from collections import Counter
import re

def extract_keywords_from_text(text, max_words=20):
    """Extract meaningful keywords from text."""
    # Remove markdown, code blocks, URLs
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'^#{1,3}\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'[^\w\s-]', ' ', text)

    # Get words, filter short ones and common stopwords
    stopwords = {'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can', 'had',
                  'her', 'was', 'one', 'our', 'out', 'with', 'have', 'been', 'will',
                  'this', 'that', 'from', 'when', 'they', 'your', 'more', 'which',
                  'their', 'would', 'about', 'than', 'into', 'just', 'what', 'some',
                  'could', 'them', 'these', 'other', 'were', 'after', 'being', 'before'}

    words = text.lower().split()
    keywords = [w for w in words if len(w) > 3 and w not in stopwords]
    return keywords[:max_words]

def generate_cluster_label(nodes, cluster_id):
    """Generate a 2-4 word label for a cluster based on its nodes."""

    if not nodes:
        return f"cluster-{cluster_id}"

    # Extract keywords from all nodes in the cluster
    all_keywords = []

    for node in nodes:
        title = node.get('title', '')
        content = node.get('content', '')
        text = f"{title} {content}"

        keywords = extract_keywords_from_text(text, max_words=10)
        all_keywords.extend(keywords)

    if not all_keywords:
        return f"cluster-{cluster_id}"

    # Count keyword frequencies
    keyword_counts = Counter(all_keywords)

    # Get top 3-5 most common keywords
    top_keywords = [kw for kw, count in keyword_counts.most_common(5)]

    # Remove similar/related keywords (keep only first occurrence of related terms)
    unique_keywords = []
    seen = set()

    for kw in top_keywords:
        # Check if keyword or its stem is already in our list
        kw_stem = kw[:4]  # Simple stemming (first 4 chars)

        if kw_stem not in seen:
            unique_keywords.append(kw)
            seen.add(kw_stem)

        if len(unique_keywords) >= 3:
            break

    # Return 2-3 keywords as label
    return ' / '.join(unique_keywords[:3])

def label_clusters():
    """Main function: read graph data, generate labels, write back."""

    print("Loading graph data...")
    with open('graph_data.json', 'r') as f:
        data = json.load(f)

    nodes_by_id = {node['id']: node for node in data.get('nodes', [])}
    clusters = data.get('clusters', [])

    print(f"Processing {len(clusters)} clusters...")

    updated_count = 0
    for i, cluster in enumerate(clusters):
        cluster_id = cluster.get('id', i)
        node_ids = cluster.get('nodes', [])

        # Get actual node objects
        cluster_nodes = [nodes_by_id.get(nid) for nid in node_ids if nid in nodes_by_id]

        # Generate label
        current_label = cluster.get('label', '')
        new_label = generate_cluster_label(cluster_nodes, cluster_id)

        if current_label != new_label:
            cluster['label'] = new_label
            updated_count += 1

        if (i + 1) % 20 == 0:
            print(f"  Processed {i+1}/{len(clusters)} clusters...")

    print(f"Updated {updated_count} cluster labels")

    # Write back
    print("Writing updated graph data...")
    with open('graph_data.json', 'w') as f:
        json.dump(data, f, indent=2)

    print("Done! Updated graph_data.json")

    # Show sample of new labels
    print("\nSample labels (first 10 clusters):")
    for cluster in clusters[:10]:
        print(f"  Cluster {cluster.get('id')}: \"{cluster.get('label')}\"")

if __name__ == '__main__':
    label_clusters()
