FROM python:3.12-slim AS builder
WORKDIR /tmp
RUN pip install poetry
COPY ./backend/pyproject.toml ./backend/poetry.lock ./
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --without dev

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /tmp/requirements.txt .
RUN pip install -r requirements.txt
COPY ./backend/app /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000
