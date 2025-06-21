from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ... import crud, schemas
from ...deps import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = crud.get_category_by_name(db, name=category.name)
    if db_category:
        raise HTTPException(status_code=400, detail="Category already registered")
    return crud.create_category(db=db, category=category)


@router.get("/", response_model=list[schemas.Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = crud.get_categories(db, skip=skip, limit=limit)
    return categories


@router.get("/stats/", response_model=list[schemas.CategoryStats])
def get_category_stats(db: Session = Depends(get_db)):
    stats = crud.get_newsletter_stats_by_category(db)
    return [
        schemas.CategoryStats(
            id=row.id,
            name=row.name,
            newsletter_count=row.newsletter_count,
        )
        for row in stats
    ]


@router.get("/{category_id}", response_model=schemas.Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category
