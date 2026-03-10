from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from ..base import Base

class MaestroBancos(Base):
    __tablename__ = 'maestro_bancos'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
