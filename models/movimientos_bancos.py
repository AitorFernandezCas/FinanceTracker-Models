from sqlalchemy import Column, Integer, Date, Float, DateTime, String
from datetime import datetime
from .base import Base

class MovimientosBancos(Base):
    __tablename__ = 'movimientos_bancos'
    fecha = Column(Date, primary_key=True)
    id_banco = Column(Integer, primary_key=True)
    concepto = Column(String(255), nullable=False)
    categoria = Column(String(255), nullable=True)
    importe = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
