
from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import liquors
from app.crud import crud_liquors
from app.api import deps
 
router = APIRouter()
 
@router.get("/liquors/", response_model=List[licores.licoreria])
def read_liquors(db: Session = Depends(deps.get_db),skip: int = 0,limit: int = 100,) -> Any:
 
    return crud_licores.get_liquors(db,skip,limit)
 
@router.post("/liquors/", response_model=licores.licoreria)
def create_item(*,db: Session = Depends(deps.get_db),liquors_in: licores.liquorsCreate,) -> Any:
   licores = crud_licores.create_licores(db=db,licores=liquors_in)
   return licores
 
@router.put("/liquors/{id}", response_model=licores.licoreria)
def update_licores(*,db: Session = Depends(deps.get_db),id: int,licores_in: licores.liquorsUpdate,) -> Any:
  
   licoresInDB = crud_licores.get(db=db, licores_id=id)
   if not licoresInDB:
       raise HTTPException(status_code=404, detail="licores not found")
  
   licores = crud_licores.update_licores(db=db,db_obj=licoresInDB,obj_in=licores_in)
   return licores
 
@router.get("/liquors/{id}", response_model=licores.licoreria)
def read_licores(*,db: Session = Depends(deps.get_db),id: int,) -> Any:
 
   licores = crud_licores.get(db=db, licores_id=id)
   if not licores:
       raise HTTPException(status_code=404, detail="licores not found")
   return licores
 
@router.delete("/liquors/{id}", response_model=licores.licoreria)
def delete_item(*,db: Session = Depends(deps.get_db),id: int,) -> Any:
 
   licores = crud_licores.get(db=db, licores_id=id)
   if not licores:
       raise HTTPException(status_code=404, detail="licores not found")
 
   licores = crud_licores.delete_licores(db=db,id=id)
   return licores
