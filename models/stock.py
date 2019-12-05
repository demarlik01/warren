from sqlalchemy.orm import relationship

from models.base import Base
from sqlalchemy import Column, Integer, String, DateTime, func


class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    code = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    # relations
    prices = relationship("Price", back_populates="stock")
    calculates = relationship("Calculate", back_populates="stock")
