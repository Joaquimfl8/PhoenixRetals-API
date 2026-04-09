from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.NotebookModel import NotebookModel
from schemas.NotebookSchema import NotebookSchema

router = APIRouter(
    prefix = "notebooks",
    tags = "notebooks"
)

@router.get("/", response_model=list[NotebookSchema])
def buscar_todos_notebooks(db: Session = Depends(get_db)):
    notebooks = db.query(NotebookModel).all()
    
    return notebooks

@router.get("/{id}", response_model=list[NotebookSchema])
def buscar_por_id_notebook(id: int, db: Session = Depends(get_db)):
    notebook = db.query(NotebookModel).filter(NotebookModel.id == id).first()
    
    if not notebook:
        raise HTTPException(status_code=404, details="Notebook não encontrado")
    
    return notebook