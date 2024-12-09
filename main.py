from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from user.routes import user_router
from product.routes import product_router
from review.routes import review_router
from auth.routes import auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name='static')
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        # Add the origins you want to allow, for example:
        "http://localhost:3000",  # React development server
        "http://localhost:8000",  # Another common development server
        "https://yourdomain.com",  # Your production frontend domain
        "*"  # Use * for allowing all origins (not recommended for production)
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


app.include_router(user_router)
app.include_router(product_router)
app.include_router(review_router)
app.include_router(auth_router)