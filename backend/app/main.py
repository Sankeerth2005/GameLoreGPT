# backend/app/main.py
from fastapi import FastAPI, HTTPException
from .schemas import LoreRequest
from .models import generate_lore

app = FastAPI(title="GameLoreGPT API")

@app.get("/")
def health():
    return {"status": "ready", "models": ["v1", "v2"]}

@app.post("/generate")
def generate(request: LoreRequest):
    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")
    lore = generate_lore(request.prompt, request.model_version)
    return {"lore": lore, "model_used": request.model_version}