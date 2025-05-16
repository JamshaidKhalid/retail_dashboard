from pydantic import BaseModel, Field
class UpdateStockRequest(BaseModel):
    product_id: int = Field(..., description="Product ID")
    new_stock: int = Field(..., ge=0, description="New stock quantity (must be non-negative)")



class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    category_id: int
    quantity: int = Field(..., gt=0)