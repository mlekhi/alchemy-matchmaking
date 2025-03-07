# using spectral clustering!!! BASED OFF OF SIMILARITY SCORES

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import SpectralClustering
import numpy as np

# Load embeddings from ChromaDB
embeddings = np.array(all_data["embeddings"])  # Shape (n_samples, embedding_dim)

# Compute cosine similarity matrix
similarity_matrix = cosine_similarity(embeddings)  # Shape (n_samples, n_samples)

# Apply Spectral Clustering using the similarity matrix
n_clusters = 3  # Adjust based on data
spectral = SpectralClustering(n_clusters=n_clusters, affinity="precomputed", random_state=42)
labels = spectral.fit_predict(similarity_matrix)

# Attach cluster labels to metadata
for i, meta in enumerate(metadata):
    meta["cluster"] = labels[i]

# Print some results
for meta in metadata[:10]:  
    print(f"Name: {meta['name']}, Question: {meta['question']}, Cluster: {meta['cluster']}")
