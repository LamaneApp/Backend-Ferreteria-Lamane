from fastapi import FastAPI
from routers import productos

app = FastAPI()

app.include_router(productos.router_product)

@app.get("/") #accedemos a app que la creamos en la linea 3. Obtenemos con get algo que esta en el lugar indicado en el corchete (en este caso solo /)
async def root(): #asincrona porque asi le indicamos que haga lo que tenga que hacer cuando pueda
    return "Hola FastAPI"