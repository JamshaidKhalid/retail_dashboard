from fastapi import APIRouter, Body
from services.product_service import register_product

router = APIRouter()

@router.post("/register")
def create_product(data: dict = Body(...)):
    return register_product(data)
