import pandas as pd
import numpy as np
import torch
from sentence_transformers import SentenceTransformer
import faiss
import json

def generate_embeddings():
    # Load SBERT Model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Constants
    CSV_FILE = "data.csv"
    COLUMN_INDEX = 1  # Adjust based on the response column
    EMBEDDINGS_FILE = "embeddings.json"
    FAISS_INDEX_FILE = "faiss_index.bin"

    print("Loading CSV...")
    df = pd.read_csv(CSV_FILE)
    responses = df.iloc[:, COLUMN_INDEX].dropna().tolist()
    names = df.iloc[:, 0].tolist()

    print("Generating embeddings...")
    embeddings = model.encode(responses, convert_to_numpy=True)

    # Normalize embeddings for similarity comparison
    embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

    # Store embeddings in FAISS for fast similarity search
    index = faiss.IndexFlatL2(embeddings.shape[1])  # L2 distance for similarity
    index.add(embeddings)

    # Save FAISS index
    faiss.write_index(index, FAISS_INDEX_FILE)

    # Save embeddings in JSON format
    embeddings_dict = {names[i]: embeddings[i].tolist() for i in range(len(names))}
    with open(EMBEDDINGS_FILE, "w") as f:
        json.dump(embeddings_dict, f, indent=4)

    print(f"Embeddings generated and saved in {EMBEDDINGS_FILE}")

if __name__ == "__main__":
    generate_embeddings()