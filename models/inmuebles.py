from sqlalchemy import Column, Date, Integer, Float, DateTime
from datetime import datetime
from .base import Base

class Inmuebles(Base):
    __tablename__ = 'inmuebles'

    fecha_seguimiento = Column(Date, primary_key=True)
    id_inmueble = Column(Integer, primary_key=True)

    valor_total = Column(Float)
    fecha_valoracion = Column(Date)
    pct_propiedad = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
