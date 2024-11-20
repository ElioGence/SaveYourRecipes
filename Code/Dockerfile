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

# Expose Flask port
EXPOSE 5000

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]