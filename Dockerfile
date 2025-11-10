# Use a lightweight base image
FROM python:3.11-alpine

# Prevent Python from writing .pyc files & buffer logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies and extra tools
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir gunicorn supervisor

# Copy all remaining project files
COPY . .

# Create supervisord configuration directly inside the image
RUN echo "[supervisord]\n\
nodaemon=true\n\
\n\
[program:web]\n\
command=gunicorn app:app -b 0.0.0.0:8080\n\
autostart=true\n\
autorestart=true\n\
\n\
[program:extractor]\n\
command=python3 -m Extractor\n\
autostart=true\n\
autorestart=true" > /etc/supervisord.conf

# Expose Render’s default web port
EXPOSE 8080

# Start both Gunicorn (Flask) and Extractor together
CMD ["supervisord", "-c", "/etc/supervisord.conf"]
