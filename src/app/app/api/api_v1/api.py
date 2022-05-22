from fastapi import APIRouter

from app.api.api_v1.endpoints import beers

api_router = APIRouter()
api_router.include_router(beers.router, prefix="/beers", tags=["beers"])

