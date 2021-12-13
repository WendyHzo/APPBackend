from sqlalchemy import Column, Integer, String
from app.database.session import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    precio= Column(Integer)
    imagen = Column(String)