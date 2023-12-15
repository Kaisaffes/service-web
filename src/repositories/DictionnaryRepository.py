from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..models.Dictionnary import Dictionnary
from ..params import DictionnaryParams, CreateDictionnaryParams, UpdateDictionnaryParams

def get_dictionnary(db: Session, params: DictionnaryParams) -> Dictionnary:
    return db.query(Dictionnary).filter(Dictionnary.id == params.id).first()

def create_dictionnary(db: Session, params: CreateDictionnaryParams) -> Dictionnary:
    created_dictionnary = Dictionnary (
        title=params.title,
        description=params.description
        )
    
    db.add(created_dictionnary)
    db.commit()
    db.refresh(created_dictionnary)
    return created_dictionnary

def update_dictionnary(db: Session, id:int ,  params: UpdateDictionnaryParams) -> Dictionnary:
    dictionnary = db.query(Dictionnary).filter(Dictionnary.id == id).first()
    if dictionnary:
        dictionnary.title = params.title
        dictionnary.description = params.description
        db.commit()
        db.refresh(dictionnary)
        return dictionnary
    else:
        raise HTTPException(status_code=404, detail="Dictionnary entry not found")

def delete_dictionnary(db: Session, id:int) -> dict:
    dictionnary = db.query(Dictionnary).filter(Dictionnary.id == id).first()
    if dictionnary:
        db.delete(dictionnary)
        db.commit()
        return {"message": "Dictionnary entry deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Dictionnary entry not found")
