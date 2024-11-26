from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates


from product.services import ProductServices
from product.repository import ProductRepository
from db import get_db

views_router = APIRouter()
templates = Jinja2Templates(directory="templates")

product_repository = ProductRepository()
product_service = ProductServices(product_repository=product_repository)

@views_router.get("/", response_class=HTMLResponse)
def render_home(request: Request, db: Session = Depends(get_db)):
    try:
        
        products = product_service.get_all_products(db=db)
        return templates.TemplateResponse(request=request, context={"title": "homepage", "products": products}, name="index.html")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error render the page")

@views_router.get("/admin-dashboard", response_class=HTMLResponse)
def render_admin(request: Request):
    try:
        return templates.TemplateResponse("admin.html", {"request": request})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error render page: {e}")
    
@views_router.get("/admin-dashboard/products", response_class=HTMLResponse)
def render_admin(request: Request):
    try:
        return templates.TemplateResponse("admin-products.html", {"request": request})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error render page: {e}")
    
@views_router.get("/admin-dashboard/users", response_class=HTMLResponse)
def render_admin(request: Request):
    try:
        return templates.TemplateResponse("admin-users.html", {"request": request})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error render page: {e}")