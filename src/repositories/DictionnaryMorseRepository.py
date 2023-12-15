from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..models.DictionnaryMorse import DictionnaryMorse  
from ..params import CreateDictionnaryParams, DictionnaryMorseParams,CreateDictionnaryMorseParams

def get_dictionnaryMorse(db: Session, text: str) -> DictionnaryMorse:
    return db.query(DictionnaryMorse).filter(DictionnaryMorse.text == text).first()

def create_dictionnaryMorse(db: Session, params: CreateDictionnaryMorseParams) -> DictionnaryMorse:
    dictionnary_morse = DictionnaryMorse (
        text = params.text,
        code_morse = params.code_morse
    )
    db.add(dictionnary_morse)
    db.commit()
    db.refresh(dictionnary_morse)
    return dictionnary_morse
