from sentence_transformers import SentenceTransformer
import faiss
import os
import pickle

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_vector_store(data_folder="data", store_path="vector_store"):
    texts, metadata = [], []

    for fname in os.listdir(data_folder):
        zodiac = fname.replace(".txt", "")
        with open(os.path.join(data_folder, fname)) as f:
            for line in f:
                texts.append(line.strip())
                metadata.append({"zodiac": zodiac})

    embeddings = model.encode(texts, convert_to_numpy=True)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    with open(f"{store_path}.pkl", "wb") as f:
        pickle.dump((index, texts, metadata), f)

    print("✅ Vector store built.")
