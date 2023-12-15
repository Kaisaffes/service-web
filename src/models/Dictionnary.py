from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from ..conf.database import Base

class Dictionnary(Base):
    __tablename__ = "dictionnary"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(40))
    description = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
