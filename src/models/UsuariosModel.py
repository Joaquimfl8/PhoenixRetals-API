from sqlalchemy import Column, Integer, Date, String
from database import Base
from sqlalchemy.orm import relationship

class NotebookModel(Base):
    __tablename__ = "Usuario"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50))
    gmail = Column(String(100))
    telefone = Column(String(11))
    ultimoAgendamento = Column(Date)
    nivelPerm = Column(Integer)
