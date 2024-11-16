# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file to the container
COPY backend/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code to the container
COPY backend/ .

# Run the application
CMD ["python", "app.py"]
