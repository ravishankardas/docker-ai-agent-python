from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from api.db import get_session  # Assuming you have a function to get DB session
from .models import ChatMessagePayload, ChatMessage, ChatMessageListItem
from api.ai.services import generate_email_message
from api.ai.schemas import EmailMessageSchema
router = APIRouter()


@router.get("/")
def chat_health_check():
    return {"message": "Chat service is running!"}

@router.get("/recent/", response_model=List[ChatMessageListItem])
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage) # sql -> query
    results = session.exec(query).fetchall()[:10]
    return results 

@router.post("/", response_model=EmailMessageSchema)
def chat_create_message(
    payload: ChatMessagePayload,
    session: Session = Depends(get_session)  # Replace with actual session dependency
):
    data = payload.model_dump()
    print(data)
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    # session.refresh(obj)
    response = generate_email_message(payload.message)
    return response