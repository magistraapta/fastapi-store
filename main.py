from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from user.routes import user_router
from product.routes import product_router
from review.routes import review_router
from fastapi.templating import Jinja2Templates
from product.services import ProductServices
from product.repository import ProductRepository
from db import get_db
from sqlalchemy.orm import Session


app = FastAPI()
templates = Jinja2Templates(directory="views")

product_repository = ProductRepository()
product_service = ProductServices(product_repository=product_repository)

@app.get("/home", response_class=HTMLResponse)
def render_home(request: Request, db: Session = Depends(get_db)):
    products = product_service.get_all_products(db=db)
    return templates.TemplateResponse(request=request, context={"title": "homepage", "products": products}, name="index.html")
    

app.include_router(user_router)
app.include_router(product_router)
app.include_router(review_router)