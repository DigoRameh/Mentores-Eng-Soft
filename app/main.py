from fastapi import FastAPI
from .database import Base, engine
from .routes import mentor_routes, agendamento_routes

app = FastAPI(title="Mentor API")

Base.metadata.create_all(bind=engine)

app.include_router(mentor_routes.router, prefix="/mentores", tags=["Mentores"])
app.include_router(agendamento_routes.router, prefix="/agendamentos", tags=["Agendamentos"])

@app.get("/")
def home():
    return {"mensagem": "API de Mentores ativa!"}
