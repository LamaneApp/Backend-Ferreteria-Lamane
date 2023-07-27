from fastapi import FastAPI
from routers import productos
from routers.ferreteria import read_file

app = FastAPI()

app.include_router(productos.router_product)

def main():
    file = "archivo ferreteria" #importar el archivo
    read_file(file)