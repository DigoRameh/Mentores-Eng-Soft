from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.MentorOut)
def criar_mentor(mentor: schemas.MentorCreate, db: Session = Depends(get_db)):
    novo_mentor = models.Mentor(**mentor.dict())
    db.add(novo_mentor)
    db.commit()
    db.refresh(novo_mentor)
    return novo_mentor

@router.get("/", response_model=list[schemas.MentorOut])
def listar_mentores(db: Session = Depends(get_db)):
    return db.query(models.Mentor).all()
