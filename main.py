from fastapi import FastAPI
import uvicorn
from routers import productos
from db.db import Base,engine

def create_tables():
    Base.metadata.create_all(bind=engine)
    
create_tables()

app = FastAPI()

app.include_router(productos.router_product)

"""if __name__=="__main__":
    uvicorn.run("main:app",port=8080,reload=True)"""
