from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime


Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(300))
    seller = Column(String(150), nullable=True)
    price = Column(String(50))
    image = Column(String(500), nullable=True)
    timestamp = Column(
        DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))
