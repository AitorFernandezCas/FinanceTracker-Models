from sqlalchemy import Column, Date, Integer, Boolean, Float, String, DateTime
from datetime import datetime
from .base import Base

class HistCompraInstrumentosFinancieros(Base):
    __tablename__ = 'hist_compra_instrumentos_financieros'

    fecha = Column(Date, primary_key=True)
    ISIN = Column(Integer, primary_key=True)
    cantidad = Column(Float)
    tipo_cambio = Column(Float)
    id_divisa = Column(String(255), nullable=True)
    comision_autoFX = Column(Float)
    coste_transaccion = Column(Float)
    valor_local = Column(Float)
    valor_EUR = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
