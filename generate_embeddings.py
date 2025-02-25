import pandas as pd
import numpy as np
import torch
from sentence_transformers import SentenceTransformer
import chromadb
import json

# decide if you wanna use SBERT
model = SentenceTransformer("all-MiniLM-L6-v2")

CSV_FILE = "data.csv"
COLUMN_INDEX = 1  # Adjust based on the response column
EMBEDDINGS_FILE = "embeddings.json"
CHROMA_DB_DIR = "chroma_db"

df = pd.read_csv(CSV_FILE)
responses = df.iloc[:, COLUMN_INDEX].dropna().tolist()
names = df.iloc[:, 0].tolist()

# Generate Embeddings
print("Generating embeddings...")
embeddings = model.encode(responses, convert_to_numpy=True)

# Normalize embeddings for similarity comparison
embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

# ChromaDB Client
chroma_client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
collection = chroma_client.get_or_create_collection(name="matchmaking")

for i, name in enumerate(names):
    collection.add(
        ids=[str(i)], 
        embeddings=[embeddings[i].tolist()], 
        metadatas=[{"name": name, "response": responses[i]}]
    )

# saving embeddings in JSON
embeddings_dict = {names[i]: embeddings[i].tolist() for i in range(len(names))}
with open(EMBEDDINGS_FILE, "w") as f:
    json.dump(embeddings_dict, f, indent=4)

print(f"Embeddings generated and stored in ChromaDB at {CHROMA_DB_DIR}")