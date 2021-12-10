from sqlalchemy import Column, Integer, String
from app.database.base_class import Base
 
class licorera(Base):
   __tablename__ = "Licores"
   id = Column(Integer, primary_key=True, index=True)
   name = Column(String, index=True)
   price = Column(Integer, index=True)
   
