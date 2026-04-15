FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# system deps
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# install deps first (cache layer)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# copy source
COPY . /app/

# non-root user
RUN useradd -m appuser && chown -R appuser /app
USER appuser

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]

# docker build -t mdzenos/django-core:1.0 .
# docker push mdzenos/django-core:1.0
