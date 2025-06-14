import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load the same model you used for embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load the stored embeddings
with open("../data/embeddings_local.pkl", "rb") as f:
    embeddings = pickle.load(f)

# Prepare lists of file paths and embedding vectors
file_paths = list(embeddings.keys())
embedding_vectors = np.array(list(embeddings.values()))

# Function to retrieve top N documents
def retrieve(query, top_k=3):
    query_embedding = model.encode([query])
    scores = cosine_similarity(query_embedding, embedding_vectors)[0]
    top_indices = scores.argsort()[-top_k:][::-1]
    
    print(f"\nTop {top_k} results for query: '{query}'")
    for idx in top_indices:
        file = file_paths[idx]
        score = scores[idx]
        print(f"\nFile: {file} (Score: {score:.4f})")
        with open(file, 'r', encoding='utf-8') as f:
            print(f.read()[:1000])  # show first 1000 characters of file

# Example query
retrieve("Explain data sourcing process in TDS")
