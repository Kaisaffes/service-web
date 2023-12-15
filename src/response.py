from datetime import datetime
from pydantic import BaseModel

class WordResponse(BaseModel):
    id: int
    text: str
    return_text: str
    created_at: datetime
    updated_at: datetime

class DictionnaryResponse(BaseModel):
    id: int 
    title: str
    description: str
    created_at: datetime
    updated_at: datetime    

class DeleteResponse(BaseModel):
    message: str

class DictionnaryMorseResponse(BaseModel):
    text: str
    code_morse: str