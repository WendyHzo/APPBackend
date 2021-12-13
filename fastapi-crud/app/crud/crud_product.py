from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session, session

from app.model.product import Product as ProductModel
from app.schema.product import ProductCreate, ProductUpdate, Product

def get_product(db: Session, product_id: int) -> ProductModel:
    """
    Obtener un producto por Id
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

def get_all_products(db: Session, skip: int = 0, limit: int = 10):
    """
    Obtener todos los productos
    """
    return db.query(ProductModel).offset(skip).limit(limit).all()

def create_product(db: Session, product: ProductCreate):
    """
    Crea un nuevo producto
    """
    db_product = ProductModel(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, *,db_ojb: ProductModel, obj_in: ProductUpdate) -> ProductModel:
    """
    Actualizar un producto
    """
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


def delete_product(db: Session, *, id: int) -> ProductModel:
    """
    Eliminar producto
    """
    obj = db.query(ProductModel).get(id)
    db.delete(obj)
    db.commit()
    return obj
