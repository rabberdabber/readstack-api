from datetime import date, datetime
from typing import Generic, TypeVar

from pydantic import BaseModel, HttpUrl
from pydantic.generics import GenericModel

from .models import CategoryName

T = TypeVar("T")


class Page(GenericModel, Generic[T]):
    items: list[T]
    total: int
    page: int
    size: int


# Category Schemas
class CategoryBase(BaseModel):
    name: CategoryName


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class CategoryStats(BaseModel):
    id: int
    name: CategoryName
    newsletter_count: int


# Newsletter Schemas
class NewsletterBase(BaseModel):
    title: str
    url: HttpUrl
    source: str = "ByteByteGo"
    published_date: date | None = None
    category_id: int


class NewsletterCreate(NewsletterBase):
    pass


class Newsletter(NewsletterBase):
    id: int
    created_at: datetime
    category: Category

    class Config:
        orm_mode = True
