from pydantic import BaseModel, EmailStr, Field

class Usuario(BaseModel):
    id: int = Field(..., gt = 0)
    nome: str = Field(..., min_length = 3)
    gmail: EmailStr
    telefone: str = Field(min_length=11, max_length=11)
    nivelPerm: int = Field(default=1, gt=0, le=5)
    