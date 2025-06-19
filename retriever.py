import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("vector_store.pkl", "rb") as f:
    index, texts, metadata = pickle.load(f)

def retrieve_chunks(query, top_k=3):
    query_embedding = model.encode([query])
    scores, indices = index.search(query_embedding, top_k)
    results = []
    for idx in indices[0]:
        results.append((texts[idx], metadata[idx]))
    return results
