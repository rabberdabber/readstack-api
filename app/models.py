import enum

from sqlalchemy import (
    TIMESTAMP,
    Column,
    Date,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy import (
    Enum as SAEnum,
)
from sqlalchemy.orm import relationship

from .database import Base


class CategoryName(enum.Enum):
    SYSTEM_DESIGN = "System Design"
    DATABASE = "Database"
    DEVOPS = "DevOps"
    DISTRIBUTED_SYSTEMS = "Distributed Systems"
    NETWORKING = "Networking"
    CACHING = "Caching"
    SCALABILITY = "Scalability"
    CLOUD_ARCHITECTURE = "Cloud Architecture"
    SECURITY = "Security"
    PERFORMANCE = "Performance"
    SOFTWARE_ENGINEERING = "Software Engineering"
    API_DESIGN = "API Design"
    MISC = "Misc"
    MICROSERVICES = "Microservices"
    DESIGN_PATTERNS = "Design Patterns"


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(SAEnum(CategoryName), unique=True, nullable=False)

    newsletters = relationship(
        "Newsletter", back_populates="category", cascade="all, delete-orphan"
    )


class Newsletter(Base):
    __tablename__ = "newsletter"

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    url = Column(String(200), nullable=False, unique=True)
    category_id = Column(
        Integer, ForeignKey("category.id", ondelete="CASCADE"), nullable=False
    )
    source = Column(String(100), nullable=False, server_default="ByteByteGo")
    published_date = Column(Date, nullable=True)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )

    category = relationship("Category", back_populates="newsletters")
