FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY wikiracer/ wikiracer/
COPY wikiracer/main.py .

CMD ["python", "main.py"]