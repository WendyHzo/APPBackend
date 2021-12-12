from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session, session

from app.model.product import Product
from app.schema.product import ProductCreate, ProductUpdate, Product

def get_product(db: Session, product_id: int) -> Product:

    " Obtener un licor por Id"
    return db.query(Product).filter(Product.id == product_id).first()

def get_all_products(db: Session, skip: int = 0, limit: int = 10):

    "Obtener todos los licor "
    return db.query(Product).offset(skip).limit(limit).all()

def create_product(db: Session, product: ProductCreate):

    "Crea un nuevo licor"
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, *,db_ojb: Product, obj_in: ProductUpdate) -> Product:

    "Actualizar un licor"
    obj_data = jsonable_encoder(db_ojb)
    if isinstance(obj_in, dict):
        update_product = obj_in
    else:
        update_data = obj_in.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(db_ojb, field, update_data[field])

    db.add(db_ojb)
    db.commit()
    db.refresh(db_ojb)
    return db_ojb


def delete_product(db: Session, *, id: int) -> Product:
   
    "Eliminar licor"
    obj = db.query(Product).get(id)
    db.delete(obj)
    db.commit()
    return obj