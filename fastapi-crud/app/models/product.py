from sqlalchemy import Column, Integer, String
from app.database.session import Base
 
class Liquors(Base):
   __tablename__ = "licores"
   id = Column(Integer, primary_key=True, index=True)
   nombre = Column(String, index=True)
   precio = Column(Integer, index=True)
   imagen = Column(String )
