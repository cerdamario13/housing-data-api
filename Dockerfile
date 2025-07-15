FROM python:3.11-slim

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only necessary source files (no __pycache__)
COPY src ./src
COPY data ./data

# Expose port if using Flask (adjust if not)
EXPOSE 8000

# Run the Flask app
CMD ["python", "src/app.py"]
