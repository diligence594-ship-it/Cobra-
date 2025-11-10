# Use a lightweight base image
FROM python:3.11-alpine

# Environment setup
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Working directory
WORKDIR /app

# Copy dependencies first
COPY requirements.txt .

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir gunicorn supervisor

# Copy all your project files
COPY . .

# Expose web port (Render requires this)
EXPOSE 8080

# Add supervisor configuration
COPY supervisord.conf /etc/supervisord.conf

# Start both web app and background services together
CMD ["supervisord", "-c", "/etc/supervisord.conf"]
