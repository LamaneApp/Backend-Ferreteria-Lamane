from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.productos import Productos
from schemas.productos_schema import Producto,ProductoUpdate


def get_all(db: Session):
    return db.query(Productos).all()

def get(id: str, db: Session):
    producto = db.query(Productos).filter(Productos.id == id).first()
    #if producto is None:
    #    raise HTTPException(status_code=400, detail="The product does not exist.")
    return producto

def get_by_supplier(proveedor:str,db:Session):
    productos_proveedor = db.query(Productos).filter(Productos.proveedor == proveedor).all()
    if productos_proveedor == []:
        raise HTTPException(status_code=404, detail="The supplier is not found.")
    return productos_proveedor

def get_by_supplier_id(codigo_proveedor:str, db:Session):
    productos = db.query(Productos).filter(Productos.codigo_proveedor == codigo_proveedor).all()
    if productos == []:
        raise HTTPException(status_code=404, detail="The supplier's id is not found.")
    return productos

def get_by_description(descripcion:str, db:Session):
    productos = db.query(Productos).filter(Productos.descripcion.contains(descripcion)).all()
    if productos == []:
        raise HTTPException(status_code=404, detail="The description's part you supplied is not found.")
    return productos

def create(producto: Producto, db: Session):
    if get(producto.id,db) is not None:
        raise HTTPException(status_code=204, detail="The product already exists.")
    producto = Productos(id=producto.id,
                         descripcion=producto.descripcion,
                         proveedor=producto.proveedor,
                         precio=producto.precio,
                         codigo_proveedor=producto.codigo_proveedor,
                         costo=producto.costo,
                         stock=producto.stock)
    db.add(producto)
    db.commit() 
    return {"detail": "The product create successfully"}

def update(producto: ProductoUpdate, db:Session):
    producto_db = db.query(Productos).filter(Productos.id == producto.id).first()
    if producto_db is None:
        raise HTTPException(status_code=400, detail="The product does not exist.")
    for key,value in producto.dict(exclude_none=True).items():
        setattr(producto_db,key,value)
    db.commit()
    return {"detail": "The product update successfully"}

def delete(id:str,db:Session):
    producto_id = db.query(Productos).filter(Productos.id==id)
    if producto_id is None:
        raise HTTPException(status_code=400, detail="The product does not exist.")
    producto_id.delete()
    db.commit()
    return {"detail": "The product delete successfully"}
    