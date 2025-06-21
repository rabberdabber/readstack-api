from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from . import models, schemas


# Category CRUD
def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def get_category_by_name(db: Session, name: str):
    return db.query(models.Category).filter(models.Category.name == name).first()


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_newsletter_stats_by_category(db: Session):
    return (
        db.query(
            models.Category.id,
            models.Category.name,
            func.count(models.Newsletter.id).label("newsletter_count"),
        )
        .join(models.Newsletter, models.Category.id == models.Newsletter.category_id)
        .group_by(models.Category.id, models.Category.name)
        .all()
    )


# Newsletter CRUD
def get_newsletter(db: Session, newsletter_id: int):
    return (
        db.query(models.Newsletter)
        .filter(models.Newsletter.id == newsletter_id)
        .first()
    )


def get_newsletters(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    category_id: int | None = None,
    sort_by: str | None = None,
    sort_order: str = "desc",
):
    query = db.query(models.Newsletter)
    if category_id:
        query = query.filter(models.Newsletter.category_id == category_id)

    total = query.with_entities(func.count()).scalar()

    if sort_by and hasattr(models.Newsletter, sort_by):
        order_column = getattr(models.Newsletter, sort_by)
        if sort_order == "desc":
            query = query.order_by(desc(order_column))
        else:
            query = query.order_by(order_column)
    else:
        # Default sort
        query = query.order_by(desc(models.Newsletter.published_date))

    newsletters = query.offset(skip).limit(limit).all()
    return newsletters, total


def create_newsletter(db: Session, newsletter: schemas.NewsletterCreate):
    db_newsletter = models.Newsletter(**newsletter.model_dump())
    db.add(db_newsletter)
    db.commit()
    db.refresh(db_newsletter)
    return db_newsletter
