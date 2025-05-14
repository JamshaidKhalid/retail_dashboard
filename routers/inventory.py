from fastapi import APIRouter, Body
from services.inventory_service import get_inventory_status, update_inventory_stock

router = APIRouter()

@router.get("/")
def inventory_status():
    return get_inventory_status()

@router.post("/update")
def update_stock(data: dict = Body(...)):
    product_id = data.get("product_id")
    new_stock = data.get("new_stock")
    return update_inventory_stock(product_id, new_stock)
