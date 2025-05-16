from fastapi import APIRouter
from models.schemas import ProductCreate
from services.product_service import register_product

router = APIRouter()

@router.post("/register")
def create_product(data: ProductCreate):
    return register_product(data)