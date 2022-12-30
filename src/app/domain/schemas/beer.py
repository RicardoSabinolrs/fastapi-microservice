from app.domain.schemas.base import BaseSchemaModel


class BeerBase(BaseSchemaModel):
    name: str
    ibu: int
    style: str
    description: str
    alcohol_tenor: str


class BeerInCreate(BeerBase):
    ...


class BeerInUpdate(BeerBase):
    ...
