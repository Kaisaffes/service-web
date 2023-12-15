from sqlalchemy.orm import Session

from ..models.Word import Word
from ..params import WordParams, CreateWordParams, UpdateWordParams

def get_word(db: Session, params: WordParams):
    word = db.query(Word).filter(Word.id == params.id).first()
    return word

def get_trad(db, text: str):
    word = db.query(Word).filter(Word.text == text).first()
    return word

def create_word(db: Session, params: CreateWordParams):
    created_word = Word(
        text=params.text,
        return_text=params.return_text,
    )
    db.add(created_word)
    db.commit()
    db.refresh(created_word)

    return created_word

def update_word(db: Session, id: int, params: UpdateWordParams):
    word = db.query(Word).filter(Word.id == id).first()
    if word: 
        word.return_text = params.return_text 
    return word


def delete_word(db: Session, id: int):
    word = db.query(Word).filter(Word.id == id).first()
    if word:
        db.delete(word)
        db.commit()
        return { "message": "Word deleted successfully" }

    return { "message": "Word not found" }
