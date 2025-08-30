# syntax=docker/dockerfile:1
FROM python:3.12-slim

# System deps (optional, keep minimal)
RUN apt-get update && apt-get install -y --no-install-recommends         build-essential         curl         && rm -rf /var/lib/apt/lists/*

# Install Poetry to manage dependencies
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir "poetry==1.8.3"

# We want Poetry to install into the system site-packages (no venv inside container)
ENV POETRY_VIRTUALENVS_CREATE=false         PYTHONDONTWRITEBYTECODE=1         PYTHONUNBUFFERED=1

WORKDIR /app

# Copy only dependency files first for better caching
COPY src/pyproject.toml ./pyproject.toml
# If you use a lock file, copy it too for reproducible builds
COPY src/poetry.lock ./poetry.lock

# Install dependencies (no project code yet)
RUN poetry install --no-root --no-interaction --no-ansi

# Copy application source
COPY src/ ./

# Default command: run the bot
CMD ["python", "main.py"]
