from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .schemas import LoreRequest
from .models import generate_lore

app = FastAPI(title="GameLoreGPT")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "GameLoreGPT API is running!"}

@app.post("/generate")
def generate(req: LoreRequest):
    try:
        lore = generate_lore(req.prompt, req.model_version or "v1")
        return {"lore": lore}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))