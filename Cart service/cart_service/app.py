from fastapi import FastAPI
from .routes.cart_routes import cart

app = FastAPI()


app.include_router(cart)

