# backend/app/models.py
from transformers import pipeline
import mlflow
import os
import time

# Model registry
MODELS = {
    "v1": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    "v2": "microsoft/Phi-3-mini-4k-instruct"
}

def get_generator(version: str = "v1"):
    model_name = MODELS.get(version, MODELS["v1"])
    try:
        return pipeline(
            "text-generation",
            model=model_name,
            device=-1,  # CPU
            max_new_tokens=256,
            do_sample=True,
            temperature=0.8,
        )
    except Exception as e:
        print(f"[FALLBACK] {model_name} failed → using TinyLlama: {e}")
        return pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", device=-1)

def generate_lore(prompt: str, version: str = "v1") -> str:
    generator = get_generator(version)
    with mlflow.start_run(run_name=f"{version}-{int(time.time())}"):
        mlflow.log_param("prompt", prompt[:100])
        mlflow.log_param("model", MODELS.get(version, "unknown"))
        mlflow.log_param("version", version)
        result = generator(f"Write a game lore: {prompt}")[0]["generated_text"]
        mlflow.log_metric("output_length", len(result))
    return result