from datetime import datetime
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, Field, HttpUrl


class DocumentCreate(BaseModel):
    url: HttpUrl

class DocumentOut(BaseModel):
    id: UUID
    url: Annotated[HttpUrl, Field(max_length=2999)]
    title: str | None = None
    status: str
    created_at: datetime

class HealthOut(BaseModel):
    status: str
    app: str
    environment: str
