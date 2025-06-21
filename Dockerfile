# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

# Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7

# 1. Base Image
FROM python:3.11-slim

# 2. Set Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3. Set workdir
WORKDIR /app

# 4. Install tools
RUN apt-get update && apt-get install -y curl --no-install-recommends && rm -rf /var/lib/apt/lists/*
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# 5. Setup venv and uv config
RUN uv venv
ENV PATH="/app/.venv/bin:$PATH"
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# 6. Install Dependencies in a cached layer
COPY pyproject.toml ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync

# 7. Copy App code
COPY ./app /app/app

# 8. Add Healthcheck
HEALTHCHECK --interval=10s --timeout=5s --retries=5 \
    CMD curl -f http://localhost:8000/health || exit 1

# 9. Expose port
EXPOSE 8000

# 10. Run App with workers
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
