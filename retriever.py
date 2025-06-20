import pickle
import os
from sentence_transformers import SentenceTransformer
from embedder import build_vector_store

model = SentenceTransformer("all-MiniLM-L6-v2")

# Build store if it doesn't exist
if not os.path.isfile("vector_store.pkl"):
    build_vector_store()

# Load the vector store
with open("vector_store.pkl", "rb") as f:
    index, texts, metadata = pickle.load(f)

def retrieve_chunks(query, top_k=3):
    query_embedding = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(query_embedding, top_k)
    results = []
    for idx in indices[0]:
        results.append((texts[idx], metadata[idx]))
    return results

