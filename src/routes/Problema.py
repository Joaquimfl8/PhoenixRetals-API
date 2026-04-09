from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.ProblemaModel import ProblemaModel
from schemas.ProblemaSchema import ProblemaSchema

router = APIRouter(
    prefix = "problemas",
    tags = "problemas"
)

@router.get("/", response_model=list[ProblemaSchema])
def buscar_todos_problemas(db: Session = Depends(get_db)):
    usuarios = db.query(ProblemaModel).all()
    
    return usuarios

@router.get("/{id}", response_model=ProblemaSchema)
def buscar_por_id_problema(id: int, db: Session = Depends(get_db)):
    usuario = db.query(ProblemaModel).filter(ProblemaModel.id == id).first()
    
    if not usuario:
        raise HTTPException(status_code=404, details="Usuario não encontrado")
    
    return usuario