# Containerize the AI-powered assistant.

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY assistant ./assistant
COPY modules ./modules
COPY main.py .

CMD ["python", "main.py"]
