# backend/Dockerfile
FROM python:3.12-slim

WORKDIR /app

RUN pip install --upgrade pip
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy ENTIRE app folder
COPY backend/app ./app
COPY frontend/streamlit_app.py .

EXPOSE 8000 8501

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 8000 & sleep 5 && streamlit run streamlit_app.py --server.port=8501 --server.headless=true"]