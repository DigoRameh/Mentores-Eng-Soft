from pydantic import BaseModel
from datetime import datetime

class MentorCreate(BaseModel):
    nome: str
    bio: str
    especialidade: str
    contato: str

class MentorOut(MentorCreate):
    id: int

    class Config:
        orm_mode = True

class AgendamentoCreate(BaseModel):
    mentor_id: int
    data_hora: datetime
    descricao: str

class AgendamentoOut(BaseModel):
    id: int
    mentor_id: int
    data_hora: datetime
    status: str
    descricao: str

    class Config:
        orm_mode = True
