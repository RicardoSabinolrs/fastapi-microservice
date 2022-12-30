from fastapi import APIRouter

from app.api.api_v1.endpoints import beer, authentication

api_router = APIRouter()
api_router.include_router(beer.router, prefix="/beers", tags=["beers"])
api_router.include_router(authentication.router, prefix="/auth", tags=["authentication"])
