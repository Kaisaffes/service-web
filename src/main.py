from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .response import WordResponse,DictionnaryResponse,DeleteResponse,DictionnaryMorseResponse
from .params import WordParams, CreateWordParams, UpdateWordParams,DictionnaryParams,CreateDictionnaryParams,UpdateDictionnaryParams,CreateDictionnaryMorseParams,DictionnaryMorseParams
from .repositories.WordRepository import get_word, get_trad, create_word, update_word, delete_word
from .repositories.DictionnaryRepository import get_dictionnary, create_dictionnary, update_dictionnary, delete_dictionnary
from .repositories.DictionnaryMorseRepository import get_dictionnaryMorse,create_dictionnaryMorse
from .conf.database import Base, SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"msg": "Hello World!"}

@app.get("/word/{id}", response_model=WordResponse)
def read_word(id: int, db: Session = Depends(get_db)):
    word_params = WordParams(id=id)
    word = get_word(db, word_params)
    return word

@app.get("/trad/{word}", response_model=WordResponse)
def read_trad(word: str, db: Session = Depends(get_db)):
    return get_trad(db, word)

@app.post("/word", response_model=WordResponse)
def create_word_route(params: CreateWordParams, db: Session = Depends(get_db)):
    created_word = create_word(db, params)
    return created_word

@app.put("/word/{id}", response_model=WordResponse)
def update_word_route(id: int, params: UpdateWordParams, db: Session = Depends(get_db)):
    updated_word = update_word(db, id, params)
    return updated_word

@app.delete("/word/{id}", response_model=DeleteResponse)
def delete_word_route(id: int, db: Session = Depends(get_db)):
   return delete_word(db, id)
    
@app.get("/dictionnary/{id}", response_model=DictionnaryResponse)
def read_dictionnary(id: int, db: Session = Depends(get_db)):
    dictionnary_params = DictionnaryParams(id=id)
    dictionnary = get_dictionnary(db, dictionnary_params)
    return dictionnary

@app.post("/dictionnary", response_model=DictionnaryResponse)
def create_dictionnary_route(params: CreateDictionnaryParams, db: Session = Depends(get_db)):
    created_dictionnary = create_dictionnary(db, params)
    return created_dictionnary

@app.put("/dictionnary/{id}", response_model=DictionnaryResponse)
def update_dictionnary_route(id: int, params: UpdateDictionnaryParams, db: Session = Depends(get_db)):
    updated_dictionnary = update_dictionnary(db, id, params)
    return updated_dictionnary

@app.delete("/dictionnary/{id}", response_model=DeleteResponse)
def delete_dictionnary_route(id: int, db: Session = Depends(get_db)):
     return  delete_dictionnary(db, id)
   
@app.get("/dictionnaryMorse/{word}", response_model=DictionnaryMorseResponse)
def read_dictionnary_morse(word: str, db: Session = Depends(get_db)):
    return get_dictionnaryMorse(db, word)


@app.post("/dictionnaryMorse", response_model=DictionnaryMorseResponse)
def create_dictionnary_morse_route(params: CreateDictionnaryMorseParams, db: Session = Depends(get_db)):
    created_dictionnary_morse = create_dictionnaryMorse(db, params)
    return created_dictionnary_morse






