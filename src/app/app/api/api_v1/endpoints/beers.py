from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Beer])
def read_beers(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
) -> Any:
    """
    Retrieve Beers.
    """
    beers = crud.beer.get_multi(db, skip=skip, limit=limit)
    return beers


@router.post("/", response_model=schemas.Beer)
def create_beer(
        *,
        db: Session = Depends(deps.get_db),
        beer_in: schemas.BeerCreate,
) -> Any:
    """
    Create new Beer.
    """
    beer = crud.beer.create(db=db, obj_in=beer_in)
    return beer


@router.put("/{id}", response_model=schemas.Beer)
def update_beer(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        beer_in: schemas.BeerUpdate
) -> Any:
    """
    Update an Beer.
    """
    beer = crud.beer.get(db=db, id=id)
    if not beer:
        raise HTTPException(status_code=404, detail="Beer not found")
    beer = crud.beer.update(db=db, db_obj=beer, obj_in=beer_in)
    return beer


@router.get("/{id}", response_model=schemas.Beer)
def read_beer(
        *,
        db: Session = Depends(deps.get_db),
        id: int
) -> Any:
    """
    Get Beer by ID.
    """
    beer = crud.beer.get(db=db, id=id)
    if not beer:
        raise HTTPException(status_code=404, detail="Beer not found")
    return beer


@router.delete("/{id}", response_model=schemas.Beer)
def delete_beer(
        *,
        db: Session = Depends(deps.get_db),
        id: int
) -> Any:
    """
    Delete an Beer.
    """
    beer = crud.beer.get(db=db, id=id)
    if not beer:
        raise HTTPException(status_code=404, detail="Beer not found")
    beer = crud.beer.remove(db=db, id=id)
    return beer
