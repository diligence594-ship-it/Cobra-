# Lightweight base image
FROM python:3.11-alpine

# Disable pyc files and buffer logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Working directory
WORKDIR /app

# Copy dependencies first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir gunicorn supervisor flask pyrogram tgcrypto

# Copy all project files
COPY . .

# Create Supervisor config (Flask + Bot)
RUN printf "[supervisord]\n\
nodaemon=true\n\n\
[program:web]\n\
command=gunicorn app:app -b 0.0.0.0:8080\n\
autostart=true\n\
autorestart=true\n\n\
[program:bot]\n\
command=python3 Extractor/main.py\n\
directory=/app\n\
autostart=true\n\
autorestart=true\n" > /etc/supervisord.conf

# Expose web port for Render
EXPOSE 8080

# Start Supervisor (runs both)
CMD [\"supervisord\", \"-c\", \"/etc/supervisord.conf\"]
