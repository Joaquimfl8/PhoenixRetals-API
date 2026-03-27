from pydantic import BaseModel
from datetime import date

class Notebook(BaseModel):
    id: int 
    bateria: int
    problemas: list[str]
    ultimoAgendamento: date