from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from ..conf.database import Base

class Word(Base):
    __tablename__ = "word"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(40))
    return_text = Column(String(200))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())