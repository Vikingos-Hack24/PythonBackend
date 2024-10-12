from fastapi import APIRouter

from services.google_cloud import call_google_service

router = APIRouter()

@router.get("/users")
def read_example():
    return {"user": "peneeeee"}

@router.get("/users/new")
def new_user():
    return {"hola": "peneeesotee"}



