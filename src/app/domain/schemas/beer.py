import datetime

from app.domain.schemas.base import BaseSchemaModel


class BeerBase(BaseSchemaModel):
    name: str
    ibu: str
    style: str
    description: str
    alcohol_tenor: str


class BeerInCreate(BeerBase):
    ...


class BeerInUpdate(BeerBase):
    ...


class BeerInResponse(BaseSchemaModel):
    id: int
    name: str
    ibu: str
    style: str
    description: str
    alcohol_tenor: str
    created_at: datetime.datetime
    updated_at: datetime.datetime | None
