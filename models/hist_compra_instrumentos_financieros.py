from sqlalchemy import Column, Date, Integer, Boolean, Float, String, DateTime
from datetime import datetime
from .base import Base

class HistCompraInstrumentosFinancieros(Base):
    __tablename__ = 'hist_compra_instrumentos_financieros'

    fecha = Column(Date, primary_key=True)
    id_instrumento = Column(Integer, primary_key=True)
    flag_compra = Column(Boolean, primary_key=True)
    cantidad = Column(Float)
    precio = Column(Float)
    id_divisa = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
