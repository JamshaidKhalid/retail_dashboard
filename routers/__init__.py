from fastapi import APIRouter
from routers.inventory import router as inventory_router
from routers.products import router as products_router
from routers.sales import router as sales_router



api_router = APIRouter()

api_router.include_router(inventory_router, prefix="/inventory", tags=["Inventory"])
api_router.include_router(products_router, prefix="/products", tags=["Products"])
api_router.include_router(sales_router, prefix="/sales", tags=["Sales"])