from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set your Vercel URL later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Memory(BaseModel):
    user_id: str
    content: str
    image_url: str = None
    voice_url: str = None
    tags: List[str] = []
    is_public: bool = False

@app.get("/")
def root():
    return {"message": "EchoHub backend running!"}

@app.post("/memories/")
def save_memory(memory: Memory):
    # save to Supabase (or for now just log)
    print(memory)
    return {"status": "success", "memory": memory}
