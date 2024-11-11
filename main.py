from fastapi import FastAPI
from user.routes import user_router
from product.routes import product_router
from review.routes import review_router

app = FastAPI()

app.include_router(user_router)
app.include_router(product_router)
app.include_router(review_router)