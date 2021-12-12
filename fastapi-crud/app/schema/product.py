from typing import Optional
from pydantic import BaseModel, AnyHttpUrl
 
# Shared properties
class liquorsBase(BaseModel):
   nombre: Optional[str] = None
   precio: Optional[int] = None
   imagen: Optional[AnyHttpUrl]
 
# Properties to receive on liquors creation
class ProductCreate(ProductBase):
    pass
    
# Properties to receive on liquors update
class ProductUpdate(ProductBase):
    pass
 
# Properties shared by models stored in DB
class ProductInDBBase(ProductBase):
    id: int
   #owner_id: int
 
   class Config:
       orm_mode = True
 
# Properties to return to client
class Product(ProductInDBBase):
    pass
 
# Properties properties stored in DB
class ProductInDB(ProductInDBBase):
    pass