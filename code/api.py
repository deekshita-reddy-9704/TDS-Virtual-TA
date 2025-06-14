from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

class QueryRequest(BaseModel):
    question: str

app = FastAPI()

# Load embedding model and FAISS index
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("embeddings", embedding_model, allow_dangerous_deserialization=True)

@app.post("/api/")
async def query_api(request: QueryRequest):
    question = request.question
    # Search top 3 relevant documents
    results = vectorstore.similarity_search(question, k=3)

    # Prepare response
    response = {
        "answer": results[0].page_content if results else "No relevant answer found.",
        "links": [
            {
                "url": f"file://{doc.metadata['source']}",
                "text": doc.page_content[:100] + "..."
            }
            for doc in results
        ]
    }
    return response
