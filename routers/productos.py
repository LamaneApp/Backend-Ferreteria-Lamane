from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db import Base, get_db,engine
from schemas.productos_schema import Producto,ProductoUpdate
import pandas as pd
from db import product
from sqlalchemy import text

Base.metadata.create_all(bind=engine)
router_product = APIRouter(prefix="/productos",tags=["productos"])

###  GETS  ###

@router_product.get("/readFile")
def lectura(db: Session = Depends(get_db)):
    data = pd.read_excel("c:/Users/laura/OneDrive/Escritorio/Ferreteria/Backend/STOCK_FERRETERIA.xlsb",sheet_name="LISTA NUESTRA DE PRECIOS",header=0)
    data = data.dropna(axis=0,thresh=5)
    for row in range(len(data)): ###--> cuando modifique el archivo (cambiar los articulos que son identicos), entonces hacer range(len(data)) en vez de 100
        product.create(Producto(id=data.iloc[row]['ARTICULO'],
                                descripcion=data.iloc[row]['DESCRIPCION'],
                                proveedor=data.iloc[row]['PROVEEDOR'],
                                precio=data.iloc[row]['P. EFECTIVO'],
                                codigo_proveedor=str(data.iloc[row]['ART. DISTRIBUIDOR']),
                                costo=data.iloc[row]['P.UNITARIO'],
                                stock=data.iloc[row]['STOCK']),db)
    return len(data)

@router_product.get("/getAll")
def get_all_products(db:Session=Depends(get_db)):
    return product.get_all(db)

@router_product.get("/get/{id}")
def get_product(id:str,db:Session=Depends(get_db)):
    return product.get(id, db)

@router_product.get('/get/productsBySupplier/')
def get_products_by_supplier(proveedor:str,db:Session=Depends(get_db)):
    return product.get_by_supplier(proveedor,db)

@router_product.get('/get/productsBySuppliersId/')
def get_products_by_supplier_id(codigo_proveedor:str,db:Session=Depends(get_db)):
    return product.get_by_supplier_id(codigo_proveedor,db)

@router_product.get('/get/productsByDescription/')
def get_products_description(descripcion:str,db:Session=Depends(get_db)):
    return product.get_by_description(descripcion,db)

###  POSTS  ###

@router_product.post("/create",status_code=201)
def create_product(producto:Producto,db:Session=Depends(get_db)):
    return product.create(producto, db)

###  PUTS  ###

@router_product.put("/update")
def update_product(producto: ProductoUpdate, db:Session=Depends(get_db)):
    return product.update(producto, db)

###  DELETES  ###

@router_product.delete("/eliminarBDD")   ###---> elimina la base entera
def delete():
    with engine.connect() as c:
        c.execute(text("DROP TABLE productos"))
        
@router_product.delete("/eliminarProducto/{id}")
def delete_product(id:str, db:Session=Depends(get_db)):
    return product.delete(id,db)
        