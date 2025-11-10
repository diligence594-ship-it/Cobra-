# Use a lightweight base image
FROM python:3.11-alpine

# Prevent .pyc and buffer issues
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Working directory
WORKDIR /app

# Copy dependency list
COPY requirements.txt .

# Install Python deps + supervisor
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir gunicorn supervisor flask pyrogram tgcrypto

# Copy all source files
COPY . .

# Create Supervisor config inline
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

# ✅ Correct CMD (works 100%)
CMD sh -c "supervisord -c /etc/supervisord.conf"
