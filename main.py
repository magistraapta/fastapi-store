from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from user.routes import user_router
from product.routes import product_router
from review.routes import review_router
from views.routes import views_router


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name='static')

app.include_router(views_router)
app.include_router(user_router)
app.include_router(product_router)
app.include_router(review_router)