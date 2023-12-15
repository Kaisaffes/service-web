from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from ..conf.database import Base

class DictionnaryMorse(Base):
    __tablename__ = "dictionnary_morse"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(40))
    code_morse = Column(String(100))