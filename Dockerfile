FROM python:3.12-slim AS builder
WORKDIR /tmp
RUN pip install uv
COPY ./pyproject.toml uv.lock ./
RUN uv export --no-dev --no-hashes --no-header --frozen > requirements.txt

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /tmp/requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt
COPY ./app /app
ENTRYPOINT ["fastapi", "run", "main.py"]
EXPOSE 8000
