from pydantic import BaseModel, Field
from datetime import date

class NotebookSchema(BaseModel):
    id: int = Field(..., ge=0)
    numero: int = Field(..., ge=0)
    bateria: int = Field(default=100, ge=0, le=100)
    problemas: list[str]
    ultimoAgendamento: date

    class Config:
        from_attributes = True