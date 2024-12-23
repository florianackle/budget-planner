FROM python:3.12-slim AS builder
WORKDIR /tmp
RUN pip install poetry
COPY ./backend/pyproject.toml ./backend/poetry.lock ./
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.12-slim
WORKDIR /backend/app
COPY --from=builder /tmp/requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt
COPY ./backend/app /app
ENTRYPOINT ["fastapi", "run", "main.py"]
EXPOSE 8000
