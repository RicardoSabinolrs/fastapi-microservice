from typing import Sequence

from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from app.api.api_v1.deps.repository import get_repository
from app.domain.repository.crud.beer import BeerCRUDRepository
from app.domain.schemas.beer import BeerInCreate, BeerInUpdate, BeerInResponse

router = APIRouter()


@router.get(
    "/",
    name="beer:all",
    response_model=Sequence[BeerInResponse],
    status_code=HTTP_200_OK
)
async def read_beers(
        beer_repo: BeerCRUDRepository = Depends(get_repository(repo_type=BeerCRUDRepository)),
):
    """
    Get All Beers.
    """
    return await beer_repo.read_beers()


@router.post(
    "/",
    name="beer:create",
    response_model=BeerInResponse,
    status_code=HTTP_201_CREATED
)
async def create_beer(
        new_beer: BeerInCreate,
        beer_repo: BeerCRUDRepository = Depends(get_repository(repo_type=BeerCRUDRepository)),
) -> BeerInResponse:
    """
    Create new Beer.
    """
    new_beer = await beer_repo.create_beer(beer_create=new_beer)

    return BeerInResponse(
        id=new_beer.id,
        name=new_beer.name,
        ibu=new_beer.ibu,
        style=new_beer.style,
        description=new_beer.description,
        alcohol_tenor=new_beer.alcohol_tenor,
        created_at=new_beer.created_at,
        updated_at=new_beer.updated_at
    )


@router.put(
    "/{id}",
    name="beer:update",
    response_model=BeerInResponse,
    status_code=HTTP_201_CREATED
)
async def update_beer(
        id: int,
        beer_update: BeerInUpdate,
        beer_repo: BeerCRUDRepository = Depends(get_repository(repo_type=BeerCRUDRepository)),
) -> BeerInResponse:
    """
    Update a Beer.
    """
    updated_beer = await beer_repo.update_beer_by_id(
        id=id,
        beer_update=beer_update
    )

    return BeerInResponse(
        id=updated_beer.id,
        name=updated_beer.name,
        ibu=updated_beer.ibu,
        style=updated_beer.style,
        description=updated_beer.description,
        alcohol_tenor=updated_beer.alcohol_tenor,
        created_at=updated_beer.created_at,
        updated_at=updated_beer.updated_at
    )


@router.get(
    "/{id}",
    name="beer:read",
    response_model=BeerInResponse,
    status_code=HTTP_200_OK
)
async def read_beer(
        id: int,
        beer_repo: BeerCRUDRepository = Depends(get_repository(repo_type=BeerCRUDRepository)),
) -> BeerInResponse:
    """
    Get Beer by ID.
    """
    beer_read = await beer_repo.read_beer_by_id(id=id)

    return BeerInResponse(
        id=beer_read.id,
        name=beer_read.name,
        ibu=beer_read.ibu,
        style=beer_read.style,
        description=beer_read.description,
        alcohol_tenor=beer_read.alcohol_tenor,
        created_at=beer_read.created_at,
        updated_at=beer_read.updated_at
    )


@router.delete(
    "/{id}",
    name="beer:delete",
    status_code=HTTP_204_NO_CONTENT
)
async def delete_beer(
        id: int,
        beer_repo: BeerCRUDRepository = Depends(get_repository(repo_type=BeerCRUDRepository)),
) -> str:
    """
    Get Beer by ID.
    """
    return await beer_repo.delete_beer_by_id(id=id)
