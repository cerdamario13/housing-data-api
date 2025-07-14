FROM python:3.11-slim

WORKDIR /app

# Copy requirements.txt from root context
COPY ../requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask source code
COPY . .

# Copy the data directory from root (if needed inside container)
COPY ../data ./data

# Expose Flask port
EXPOSE 8000

# Run the Flask app
CMD ["python", "app.py"]
