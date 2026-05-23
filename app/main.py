from fastapi import FastAPI
from pydantic import BaseModel

from app.rag.generator import get_qa_chain


app = FastAPI(
    title="Enterprise RAG Chatbot API"
)


# Load QA chain once during startup
qa_chain = get_qa_chain()


class ChatRequest(BaseModel):
    question: str


@app.get("/")
def home():

    return {
        "message": "Enterprise RAG Chatbot API Running"
    }


@app.post("/chat")
async def chat(request: ChatRequest):

    response = qa_chain.invoke({
        "query": request.question
    })

    answer = response["result"]

    sources = []

    for doc in response["source_documents"]:

        sources.append({
            "source": doc.metadata.get("source"),
            "page": doc.metadata.get("page")
        })

    return {
        "question": request.question,
        "answer": answer,
        "sources": sources
    }