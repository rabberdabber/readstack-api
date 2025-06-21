from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Literal
from ... import crud, schemas
from ...deps import get_db, pagination_params

router = APIRouter()

SortByField = Literal["published_date", "created_at", "source", "title"]


@router.post("/", response_model=schemas.Newsletter)
def create_newsletter(
    newsletter: schemas.NewsletterCreate, db: Session = Depends(get_db)
):
    return crud.create_newsletter(db=db, newsletter=newsletter)


@router.get("/", response_model=schemas.Page[schemas.Newsletter])
def read_newsletters(
    db: Session = Depends(get_db),
    pagination: dict = Depends(pagination_params),
    category_id: int | None = Query(None, description="Filter by category ID"),
    sort_by: SortByField = Query("published_date", description="Field to sort by"),
    sort_order: Literal["asc", "desc"] = Query("desc", description="Sort order"),
):
    newsletters, total = crud.get_newsletters(
        db,
        skip=pagination["skip"],
        limit=pagination["limit"],
        category_id=category_id,
        sort_by=sort_by,
        sort_order=sort_order,
    )
    return schemas.Page(
        items=newsletters,
        total=total,
        page=pagination["page"],
        size=pagination["limit"],
    )


@router.get("/{newsletter_id}", response_model=schemas.Newsletter)
def read_newsletter(newsletter_id: int, db: Session = Depends(get_db)):
    db_newsletter = crud.get_newsletter(db, newsletter_id=newsletter_id)
    if db_newsletter is None:
        raise HTTPException(status_code=404, detail="Newsletter not found")
    return db_newsletter
