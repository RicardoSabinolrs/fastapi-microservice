from app.crud.base import CRUDBase
from app.models.beer import Beer
from app.schemas.beer import BeerCreate, BeerUpdate


class CRUDBeer(CRUDBase[Beer, BeerCreate, BeerUpdate]):
    ...


beer = CRUDBeer(Beer)
