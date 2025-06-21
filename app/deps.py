from fastapi import Query
from .database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def pagination_params(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(10, ge=1, le=100, description="Page size"),
):
    return {"page": page, "size": size, "skip": (page - 1) * size, "limit": size}
