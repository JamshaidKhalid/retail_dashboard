from fastapi import APIRouter, Query
from typing import Optional
from services.sales_service import get_sales_data, get_revenue_summary

router = APIRouter()

@router.get("/")
def fetch_sales(start_date: Optional[str] = None, end_date: Optional[str] = None):
    return get_sales_data(start_date, end_date)

@router.get("/revenue")
def revenue_summary(period: str = Query(..., enum=["daily", "weekly", "monthly", "yearly"])):
    return get_revenue_summary(period)
