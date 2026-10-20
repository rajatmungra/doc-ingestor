from datetime import UTC, datetime
from uuid import uuid4

from fastapi import FastAPI, status

from doc_ingestor.config import settings
from doc_ingestor.schemas import DocumentCreate, DocumentOut, HealthOut

app = FastAPI(title=settings.app_name)

@app.get("/health")
def health() -> HealthOut:
    return HealthOut(status="ok", app=settings.app_name, environment=settings.environment)

@app.post("/documents", status_code=status.HTTP_201_CREATED)
def create_document(payload: DocumentCreate) -> DocumentOut:
    return DocumentOut(
        id=uuid4(),
        url=payload.url,
        status="pending",
        created_at=datetime.now(UTC),
    )

