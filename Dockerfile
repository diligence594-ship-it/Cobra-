# Use a lightweight base image
FROM python:3.11-alpine

# Environment setup
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir gunicorn supervisor

# Copy your project files
COPY . .

# Create proper supervisord.conf with clean newlines
RUN printf "[supervisord]\n" > /etc/supervisord.conf && \
    printf "nodaemon=true\n\n" >> /etc/supervisord.conf && \
    printf "[program:web]\n" >> /etc/supervisord.conf && \
    printf "command=gunicorn app:app -b 0.0.0.0:8080\n" >> /etc/supervisord.conf && \
    printf "autostart=true\n" >> /etc/supervisord.conf && \
    printf "autorestart=true\n\n" >> /etc/supervisord.conf && \
    printf "[program:extractor]\n" >> /etc/supervisord.conf && \
    printf "command=python3 -m Extractor\n" >> /etc/supervisord.conf && \
    printf "autostart=true\n" >> /etc/supervisord.conf && \
    printf "autorestart=true\n" >> /etc/supervisord.conf

# Expose port 8080 for Render
EXPOSE 8080

# Start Supervisor
CMD ["supervisord", "-c", "/etc/supervisord.conf"]

# Start both Gunicorn (Flask) and Extractor together
CMD ["supervisord", "-c", "/etc/supervisord.conf"]
