import os
import glob
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from sentence_transformers import SentenceTransformer

# Path where your extracted files are stored
BASE_PATH = "../data/"

# Model for embeddings
model_name = "sentence-transformers/all-MiniLM-L6-v2"
embedding_model = HuggingFaceEmbeddings(model_name=model_name)

# Load all text files
documents = []
for filepath in glob.glob(BASE_PATH + "**/*.txt", recursive=True):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        documents.append(Document(page_content=content, metadata={"source": filepath}))
    print(f"Reading: {filepath}")

# Create FAISS index
vectorstore = FAISS.from_documents(documents, embedding_model)

# Save the index
os.makedirs("embeddings", exist_ok=True)
vectorstore.save_local("embeddings")

print("✅ All embeddings generated and FAISS index saved!")
