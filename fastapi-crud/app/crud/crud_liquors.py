from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.models.liquors import licoreria
from app.schemas.liquors import liquorsCreate, liquorsUpdate
 
"""obtiene un licor por el id"""
def get(db:Session, licores_id:int) -> licoreria:
   return db.query(licoreria).filter(licores.id == licores_id).first()
 
"""Obtener todos los licores"""
def get_liquors(db:Session, skip: int = 0, limit: int = 10):
   return db.query(licoreria).offset(skip).limit(limit).all()
 
"""Crear un licor"""
def create_liquors(db:Session, licoreria: liquorsCreate):
   db_licores = licoreria(**licores.dict())
   db.add(db_licores)
   db.commit()
   db.refresh(db_licores)
   return db_licores
 
"""Actualizar un licor"""
def update_liquors(db:Session, *,db_obj:licoreria, obj_in: liquorsUpdate)-> licoreria:
   obj_data = jsonable_encoder(db_obj)
   if isinstance(obj_in,dict):
       update_data = obj_in
   else:
       update_data = obj_in.dict(exclude_unset=True)
   for field in obj_data:
       if field in update_data:
           setattr(db_obj,field, update_data[field])
 
   db.add(db_obj)
   db.commit()
   db.refresh(db_obj)
   return db_obj
 
"""Eliminar un licor"""
def delete_liquors (db:Session, *, id: int)->licoreria:
   obj = db.query(licoreria).get(id)
   db.delete(obj)
   db.commit()
   return obj