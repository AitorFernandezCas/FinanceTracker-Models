from sqlalchemy import Column, Integer, Date, Float, DateTime
from datetime import datetime
from .base import Base

class Liquidez(Base):
    __tablename__ = 'liquidez'

    id_usuario = Column(Integer, primary_key=True)
    fecha_seguimiento = Column(Date, primary_key=True)
    id_banco = Column(Integer, primary_key=True)

    importe = Column(Float, nullable=False)
    rendimiento = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
