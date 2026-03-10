from sqlalchemy import Column, Integer, Date, Float, DateTime
from datetime import datetime
from .base import Base

class Deudas(Base):
    __tablename__ = 'deudas'

    id_deuda = Column(Integer, primary_key=True)
    fecha = Column(Date, primary_key=True)

    valor_total = Column(Float)
    porcentaje = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
