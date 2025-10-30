# backend/app/schemas.py
from pydantic import BaseModel
from typing import Optional

class LoreRequest(BaseModel):
    prompt: str
    model_version: Optional[str] = "v1"
    model_config = {"protected_namespaces": ()}