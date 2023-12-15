from pydantic import BaseModel

class WordParams(BaseModel):
    id: int

class CreateWordParams(BaseModel):
    text: str
    return_text: str

class UpdateWordParams(BaseModel):
    return_text: str
    
class DictionnaryParams(BaseModel):
    id: int

class CreateDictionnaryParams(BaseModel):
    title: str
    description: str

class UpdateDictionnaryParams(BaseModel):
    title: str
    description: str

class DictionnaryMorseParams(BaseModel):
    text: str
    code_morse: str

class CreateDictionnaryMorseParams(BaseModel):
    text: str
    code_morse: str
