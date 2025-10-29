from pydantic import BaseModel, Field, ConfigDict

class LoreRequest(BaseModel):
    model_version: str
    prompt: str

    model_config = ConfigDict(protected_namespaces=())