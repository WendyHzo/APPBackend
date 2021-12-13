from os import SEEK_CUR
from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schema import product
from app.crud import crud_product
from app.api import deps

router = APIRouter()
@router.get("/products/", response_model=List[product.Product])
def read_product(db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 10) -> Any:
    return crud_product.get_all_products(db=db, skip=skip, limit=limit)

@router.post("/products/", response_model=product.Product)
def create_product(*,db: Session = Depends(deps.get_db), product_in: product.ProductCreate) -> Any:
    place = crud_product.create_product(db=db, product=product_in)
    return place


@router.put("/products/{id}", response_model=product.Product)
def update_product(*,db: Session = Depends(deps.get_db), id: int, product_in: product.ProductUpdate) -> Any:
    productInDB = crud_product.get_product(db, product_id=id)
    if not productInDB:
        raise HTTPException(status_code=404, detail="Product not found")
    product = crud_product.update_product(db=db, db_ojb=productInDB, obj_in=product_in)
    return product


@router.get("/products/{id}", response_model=product.Product)
def read_product(*,db: Session = Depends(deps.get_db), id: int) -> Any:
    product = crud_product.get_product(db=db, product_id=id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.delete("/products/{id}", response_model=product.Product)
def delete_product(*,db: Session = Depends(deps.get_db), id: int) -> Any:
    product = crud_product.get_product(db=db, product_id=id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product = crud_product.delete_product(db=db, id=id)
    return product