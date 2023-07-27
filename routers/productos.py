from fastapi import APIRouter
from routers.ferreteria import read_file

router_product = APIRouter(prefix="/productos",tags=["productos"])

@router_product.get("/")
def get_all_products():
    return lectura
