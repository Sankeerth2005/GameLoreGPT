from transformers import pipeline
import mlflow
import os

MODEL_NAME = os.getenv("LLM_MODEL", "TinyLlama/TinyLlama-1.1B-Chat-v1.0")

generator = pipeline(
    "text-generation",
    model=MODEL_NAME,
    device=-1,  # CPU
    max_new_tokens=256,
    do_sample=True,
    temperature=0.8,
)

def generate_lore(prompt: str, version: str = "v1") -> str:
    with mlflow.start_run(run_name=version):
        mlflow.log_param("prompt", prompt[:100])
        result = generator(prompt)[0]["generated_text"]
        mlflow.log_metric("output_length", len(result))
    return result