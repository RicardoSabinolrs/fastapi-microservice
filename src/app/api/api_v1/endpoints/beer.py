from typing import Sequence

from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from app.api.api_v1.deps.repository import get_repository
from app.domain.models.beer import Beer
from app.domain.repository.crud.beer import BeerCRUDRepository
from app.domain.schemas.beer import BeerInCreate, BeerInUpdate

router = APIRouter()


@router.get(
    "/",
    name="beer:all",
    response_model=Sequence[Beer],
    status_code=HTTP_200_OK
)
def read_beers(
        beer_repo: BeerCRUDRepository = Depends(get_repository(repo_type=BeerCRUDRepository)),
) -> Sequence[Beer]:
    """
    Get All Beers.
    """
    return await beer_repo.read_beers()


@router.post(
    "/",
    name="beer:create",
    response_model=Beer,
    status_code=HTTP_201_CREATED
)
async def create_beer(
        beer_create: BeerInCreate,
        beer_repo: BeerCRUDRepository = Depends(get_repository(repo_type=BeerCRUDRepository)),
) -> Beer:
    """
    Create new Beer.
    """
    return await beer_repo.create_beer(
        beer_create=beer_create
    )


@router.put(
    "/{id}",
    name="beer:update",
    response_model=Beer,
    status_code=HTTP_201_CREATED
)
def update_beer(
        id: int,
        beer_update: BeerInUpdate,
        beer_repo: BeerCRUDRepository = Depends(get_repository(repo_type=BeerCRUDRepository)),
) -> Beer:
    """
    Update a Beer.
    """
    return await beer_repo.update_beer_by_id(
        id=id,
        beer_update=beer_update
    )


@router.get(
    "/{id}",
    name="beer:read",
    response_model=Beer,
    status_code=HTTP_200_OK
)
def read_beer(
        id: int,
        beer_repo: BeerCRUDRepository = Depends(get_repository(repo_type=BeerCRUDRepository)),
) -> Beer:
    """
    Get Beer by ID.
    """
    return await beer_repo.read_beer_by_id(id=id)


@router.delete(
    "/{id}",
    name="beer:delete",
    status_code=HTTP_204_NO_CONTENT
)
def delete_beer(
        id: int,
        beer_repo: BeerCRUDRepository = Depends(get_repository(repo_type=BeerCRUDRepository)),
) -> str:
    """
    Get Beer by ID.
    """
    return await beer_repo.delete_beer_by_id(id=id)
