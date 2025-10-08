FROM python:3.11-slim
WORKDIR /app/src

COPY requirements.txt ../requirements.txt
RUN pip install --no-cache-dir -r ../requirements.txt

COPY src .
COPY data ./data

EXPOSE 8000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
