from sqlalchemy import Column, Integer, Text, Boolean, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, declared_attr, relationship
from datetime import datetime


class Base(DeclarativeBase):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    is_active = Column(Boolean, default=True)
    date_created = Column(DateTime, default=datetime.utcnow)
    date_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class Category(Base):
    name = Column(String(80), unique=True)

    products = relationship("Product", backref="category", lazy=True)
    
    def __str__(self):
        return self.name


class Product(Base):
    title = Column(String(100), unique=True)
    description = Column(Text, nullable=True)
    price = Column(Float, default=0.00)

    category_id = Column(Integer, ForeignKey(Category.id))

    def __str__(self):
        return self.title
