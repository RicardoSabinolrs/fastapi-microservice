from sqlalchemy.orm import Session

from app import crud
from app.schemas.beer import BeerCreate
from app.tests.utils.utils import random_lower_string


def test_create_beer(db: Session) -> None:
    name = random_lower_string()
    ibu = random_lower_string()
    style = random_lower_string()
    description = random_lower_string()
    alcohol_tenor = random_lower_string()

    beer_in = BeerCreate(
        name=name,
        ibu=ibu,
        style=style,
        description=description,
        alcohol_tenor=alcohol_tenor
    )
    beer = crud.beer.create(db=db, obj_in=beer_in)
    assert beer.name == name
    assert beer.ibu == ibu
    assert beer.style == style
    assert beer.description == description
    assert beer.alcohol_tenor == alcohol_tenor
