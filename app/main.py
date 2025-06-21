from fastapi import FastAPI

from .api.routers import categories, newsletters
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Readstack API")

app.include_router(newsletters.router, prefix="/newsletters", tags=["newsletters"])
app.include_router(categories.router, prefix="/categories", tags=["categories"])


@app.get("/")
def read_root():
    return {"message": "Welcome to Readstack API"}


@app.get("/health", status_code=200)
def health_check():
    """
    Health check endpoint.
    """
    return {"status": "ok"}
