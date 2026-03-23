from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from ..base import Base

class MaestroActivosFinancieros(Base):
    __tablename__ = 'maestro_activos_financieros'

    id = Column(Integer)
    isin = Column(String(255), primary_key=True)
    id_tipo_instrumento = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
