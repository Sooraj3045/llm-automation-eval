
from fastapi import FastAPI
from pydantic import BaseModel

from database import create_table, save_chat, get_all_chats

app = FastAPI(
    title="BiteSpeed Support API",
    description="API for customer support chatbot testing",
    version="1.0"
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@app.on_event("startup")
def startup():
    create_table()


@app.get("/")
def home():
    return {"message": "BiteSpeed Support API is running"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    message = request.message.lower()

    if "late" in message or "delay" in message:
        response = (
            "Orders delayed by more than 45 minutes "
            "are eligible for a full refund or voucher."
        )

    elif "missing" in message:
        response = (
            "Missing items are eligible for a refund "
            "or replacement voucher."
        )

    else:
        response = (
            "Unable to determine the applicable policy. "
            "Please contact customer support."
        )

    save_chat(request.message, response)

    return {"response": response}


@app.get("/history")
def chat_history():
    return {"chats": get_all_chats()}
