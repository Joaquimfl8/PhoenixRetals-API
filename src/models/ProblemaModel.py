from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class ProblemaModel(Base):
    __tablename__ = "problema"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(50))
    notebook_id = Column(Integer, ForeignKey("notebook.id"))
    dono = relationship("NotebookModel", back_populates="problemas")
