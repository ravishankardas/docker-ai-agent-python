from fastapi import FastAPI
import os
app = FastAPI()


MY_PROJECT = os.environ.get("MY_PROJECT", "default_project")
API_KEY = os.environ.get("API_KEY", "default_key")

if not API_KEY:
    raise ValueError("API_KEY environment variable is not set.")

@app.get("/")
def read_root():
    return {"message": "Hello, World again!"}