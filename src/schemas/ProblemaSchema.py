from pydantic import BaseModel, Field
from datetime import date

class ProblemaSchema(BaseModel):
    id: int = Field(..., ge=0)
    descricao = str = Field(..., min_length=5, max_length=50)

    class Config:
        from_attributes = True