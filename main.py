from fastapi import FastAPI
from api.endpoints import user_endpoint

app = FastAPI()

app.include_router(user_endpoint.router)