from fastapi import FastAPI
from .routes.provider_routes import provider

app = FastAPI()


app.include_router(provider)

