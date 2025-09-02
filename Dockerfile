FROM python:3.11-slim-bookworm

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY task_api ./task_api/
CMD ["python", "-m", "task_api.app"]