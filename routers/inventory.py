from fastapi import APIRouter, Body
from services.inventory_service import get_inventory_status, update_inventory_stock
from models.schemas import UpdateStockRequest

router = APIRouter()


@router.get("/")
def inventory_status(quantity_threshold: int = 50):
    return get_inventory_status(quantity_threshold)


@router.patch("/update")
def update_stock(data: UpdateStockRequest):
    return update_inventory_stock(data.product_id, data.new_stock)
