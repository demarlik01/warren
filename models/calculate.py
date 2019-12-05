from sqlalchemy.orm import relationship

from models.base import Base
from sqlalchemy import Column, Integer, REAL, DateTime, func, ForeignKey


class Calculate(Base):
    __tablename__ = 'calculate'

    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey('stock.id'))
    sd = Column(REAL)
    mean = Column(REAL)
    created_at = Column(DateTime, server_default=func.now())

    # relations
    stock = relationship('Stock', back_populates="calculates")
