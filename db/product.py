from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.productos import Productos
from schemas.productos_schema import Producto,ProductoUpdate


def get_all(db: Session):
    return db.query(Productos).all()

def get(id: str, db: Session):
    return db.query(Productos).filter(Productos.id == id).first()

def create(producto: Producto, db: Session):
    producto = Productos(id=producto.id,
                         descripcion=producto.descripcion,
                         proveedor=producto.proveedor,
                         precio=producto.precio,
                         codigo_proveedor=producto.codigo_proveedor,
                         costo=producto.costo,
                         stock=producto.stock)
    db.add(producto)
    db.commit() #--> esto es para actualizar la base manualmente por si hay algun problema
    return producto

def update(producto: ProductoUpdate, db:Session):
    producto_db = db.query(Productos).filter(Productos.id == producto.id).first()
    for key,value in producto.dict(exclude_none=True).items():
        setattr(producto_db,key,value)
    db.commit()
    return producto
    