from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from ..base import Base

class MaestroDivisas(Base):
    __tablename__ = 'maestro_divisas'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
