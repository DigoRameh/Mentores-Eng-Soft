from fastapi import FastAPI
from .database import Base, engine
from .routes import mentor_routes, agendamento_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Mentor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["mentores-gqgegpddgjdwb7aw.brazilsouth-01.azurewebsites.net"],
    allow_credentials=True,
    allow_methods=["mentores-gqgegpddgjdwb7aw.brazilsouth-01.azurewebsites.net"],
    allow_headers=["mentores-gqgegpddgjdwb7aw.brazilsouth-01.azurewebsites.net"],
)

Base.metadata.create_all(bind=engine)

app.include_router(mentor_routes.router, prefix="/mentores", tags=["Mentores"])
app.include_router(agendamento_routes.router, prefix="/agendamentos", tags=["Agendamentos"])

@app.get("/")
def home():
    return {"mensagem": "API de Mentores ativa!"}
