import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer

# Load the sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

def split_text_into_chunks(text, chunk_size=300, overlap=100):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = words[i:i+chunk_size]
        chunks.append(" ".join(chunk))
        i += chunk_size - overlap
    return chunks

def build_vector_store(txt_file="text.txt", store_path="vector_store"):
    if not os.path.isfile(txt_file):
        raise FileNotFoundError(f" File {txt_file} not found in current directory.")
    
    # Read the large astrology text file
    with open(txt_file, "r", encoding="utf-8") as f:
        full_text = f.read()

    # Split into overlapping chunks
    chunks = split_text_into_chunks(full_text)
    metadata = [{"chunk_id": i} for i in range(len(chunks))]

    # Generate embeddings
    embeddings = model.encode(chunks, convert_to_numpy=True)

    # Create correct FAISS index for similarity search
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    # Save the index and metadata
    with open(f"{store_path}.pkl", "wb") as f:
        pickle.dump((index, chunks, metadata), f)

    print(f"Vector store built with {len(chunks)} chunks from {txt_file}.")
