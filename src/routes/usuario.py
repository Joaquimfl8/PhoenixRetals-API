from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.UsuariosModel import UsuarioModel
from schemas.usuario import UsuarioSchema

router = APIRouter(
    prefix = "usuarios",
    tags = "usuarios"
)

@router.get("/", response_model=list[UsuarioSchema])
def buscar_todos_notebooks(db: Session = Depends(get_db)):
    usuarios = db.query(UsuarioModel).all()
    
    return usuarios

@router.get("/{id}", response_model=UsuarioSchema)
def buscar_por_id_notebook(id: int, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioModel).filter(UsuarioModel.id == id).first()
    
    if not usuario:
        raise HTTPException(status_code=404, details="Usuario não encontrado")
    
    return usuario