from sqlalchemy import Column, Float, Integer, String
from db.db import Base


class Productos(Base):
    __tablename__ = "productos"
    id = Column(String,primary_key=True, index=True)
    descripcion = Column(String)
    proveedor = Column(String)
    precio = Column(Float)
    codigo_proveedor = Column(String)
    costo = Column(Float)
    stock = Column(Integer)