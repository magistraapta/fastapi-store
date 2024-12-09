from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from user.routes import user_router
from product.routes import product_router
from review.routes import review_router
from auth.routes import auth_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name='static')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(user_router)
app.include_router(product_router)
app.include_router(review_router)
app.include_router(auth_router)