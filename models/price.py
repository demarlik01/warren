from models.base import Base
from sqlalchemy import Column, Integer, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship


class Price(Base):
    __tablename__ = 'price'

    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey('stock.id'))
    price = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    # relations
    stock = relationship('Stock', back_populates="prices")
