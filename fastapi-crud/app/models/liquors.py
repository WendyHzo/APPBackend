from sqlalchemy import Column, Integer, String
from app.database.base_class import Base
 
class licoreria(Base):
   __tablename__ = "licores"
   id = Column(Integer, primary_key=True, index=True)
   nombre = Column(String, index=True)
   precio = Column(Integer, index=True)
   imagen = Column(String )
