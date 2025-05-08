from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.AgendamentoOut)
def criar_agendamento(agendamento: schemas.AgendamentoCreate, db: Session = Depends(get_db)):
    mentor = db.query(models.Mentor).filter(models.Mentor.id == agendamento.mentor_id).first()
    if not mentor:
        raise HTTPException(status_code=404, detail="Mentor não encontrado")
    novo_agendamento = models.Agendamento(**agendamento.dict())
    db.add(novo_agendamento)
    db.commit()
    db.refresh(novo_agendamento)
    return novo_agendamento

@router.get("/", response_model=list[schemas.AgendamentoOut])
def listar_agendamentos(db: Session = Depends(get_db)):
    return db.query(models.Agendamento).all()

@router.put("/{agendamento_id}/status", response_model=schemas.AgendamentoOut)
def atualizar_status_agendamento(agendamento_id: int, status: str, db: Session = Depends(get_db)):
    agendamento = db.query(models.Agendamento).filter(models.Agendamento.id == agendamento_id).first()
    if not agendamento:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    if status not in ["aceito", "rejeitado"]:
        raise HTTPException(status_code=400, detail="Status inválido")
    agendamento.status = status
    db.commit()
    db.refresh(agendamento)
    return agendamento
