from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.beer import BeerCreate
from app.tests.utils.utils import random_lower_string


def create_random_beer(db: Session) -> models.Beer:
    name = random_lower_string()
    ibu = random_lower_string()
    style = random_lower_string()
    description = random_lower_string()
    alcohol_tenor = random_lower_string()

    beer_in = BeerCreate(
        id=id,
        name=name,
        ibu=ibu,
        style=style,
        description=description,
        alcohol_tenor=alcohol_tenor
    )
    return crud.beer.create(
        db=db,
        obj_in=beer_in
    )
