from pydantic import BaseModel
from typing import Optional

class Producto(BaseModel):
    id: str
    descripcion: str
    proveedor: str
    precio: float
    codigo_proveedor: Optional[str]=None
    costo: float
    stock: int
    
class ProductoUpdate(BaseModel):
    id: str
    descripcion: Optional[str]=None
    proveedor: Optional[str]=None
    precio: Optional[float]=None
    codigo_proveedor: Optional[str]=None
    costo: Optional[float]=None
    stock: Optional[int]=None
    class Config:
        orm_mode=True