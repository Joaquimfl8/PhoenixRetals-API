from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    nome: str
    gmail: str
    telefone: str
    nivelPerm: int
    