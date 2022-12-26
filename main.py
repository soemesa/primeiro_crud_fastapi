from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from models import Curso
from database import engine, Base, get_db
from repositories import CursoRepository
from schemas import CursoRequest, CursoResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/api/cursos", response_model=CursoResponse, status_code=status.HTTP_201_CREATED)
def create(request: CursoRequest, db: Session = Depends(get_db)):
    curso = CursoRepository.save(db, Curso(**request.dict()))
    return CursoResponse.from_orm(curso)
