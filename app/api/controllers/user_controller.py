
from fastapi import APIRouter


user = APIRouter()

@user.get("/app")
def appStatus():
    return {"staus": "running"}