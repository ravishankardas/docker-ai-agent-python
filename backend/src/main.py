import os
from contextlib import asynccontextmanager
from fastapi import FastAPI

from api.db import init_db
from api.chat.routing import router as chat_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan event handler."""
    init_db()
    yield
    # Cleanup actions can be added here if needed


app = FastAPI(lifespan=lifespan)
app.include_router(chat_router, prefix="/api/chats", tags=["chat"])

MY_PROJECT = os.environ.get("MY_PROJECT", "default_project")
API_KEY = os.environ.get("API_KEY", "default_key")

if not API_KEY:
    raise ValueError("API_KEY environment variable is not set.")

@app.get("/")
def read_root():
    return {"message": "Hello, World again!"}