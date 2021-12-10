from typing import Optional
 
from pydantic import BaseModel, AnyHttpUrl
 
# Shared properties
class liquorsBase(BaseModel):
   nombre: Optional[str] = None
   precio: Optional[int] = None
   imagen: Optional[AnyHttpUrl]
 
# Properties to receive on liquors creation
class liquorsCreate(liquorsBase):
   pass
 
# Properties to receive on liquors update
class liquorsUpdate(liquorsBase):
   pass
 
# Properties shared by models stored in DB
class liquorsInDBBase(liquorsBase):
   id: int
   #owner_id: int
 
   class Config:
       orm_mode = True
 
# Properties to return to client
class liquors(liquorsInDBBase):
   pass
 
# Properties properties stored in DB
class liquorsInDB(liquorsInDBBase):
   pass
