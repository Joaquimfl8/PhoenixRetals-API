from sqlalchemy import Column, Integer, Date
from database import Base
from sqlalchemy.orm import relationship

class NotebookModel(Base):
    __tablename__ = "notebook"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(Integer, unique=True)
    bateria = Column(Integer, default=100)
    problemas = relationship("ProblemaModel", back_populates="dono")
    ultimoAgendamento = Column(Date)
