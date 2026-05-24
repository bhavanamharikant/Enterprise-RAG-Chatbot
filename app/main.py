from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from app.rag.langgraph_flow import graph


app = FastAPI(
    title="Enterprise RAG Chatbot API"
)


class ChatRequest(BaseModel):
    question: str


@app.get("/")
def home():

    return {
        "message": "Enterprise RAG Chatbot API Running"
    }


@app.post("/chat")
async def chat(request: ChatRequest):

    async def generate_response():

        result = graph.invoke({

            "question": request.question

        })

        answer = result["answer"]

        for word in answer.split():

            yield word + " "

    return StreamingResponse(
        generate_response(),
        media_type="text/plain"
    )