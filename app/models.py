from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class Mentor(Base):
    __tablename__ = "mentores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    bio = Column(Text)
    especialidade = Column(String)
    contato = Column(String)

    agendamentos = relationship("Agendamento", back_populates="mentor")

class Agendamento(Base):
    __tablename__ = "agendamentos"
    id = Column(Integer, primary_key=True, index=True)
    mentor_id = Column(Integer, ForeignKey("mentores.id"))
    data_hora = Column(DateTime, nullable=False)
    status = Column(String, default="pendente")  # pendente, aceito, rejeitado
    descricao = Column(Text)

    mentor = relationship("Mentor", back_populates="agendamentos")
