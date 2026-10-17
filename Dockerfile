FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml README.md LICENSE ./
COPY src ./src
RUN pip install --no-cache-dir .
EXPOSE 8000
# Local demo only: add authentication and authorization before any network deployment.
CMD ["uvicorn", "elima_early_warning.api:app", "--host", "0.0.0.0", "--port", "8000"]
