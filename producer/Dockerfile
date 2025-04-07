FROM python:3.12.7-slim

# Установка poetry
RUN pip install poetry

WORKDIR /app


COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install --no-root --only main

COPY producer/ .
ENTRYPOINT ["poetry", "run", "python", "main.py"]