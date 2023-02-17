import datetime

from app.domain.schemas.base import BaseSchemaModel


class BeerBase(BaseSchemaModel):
    name: str
    ibu: str
    style: str
    description: str
    alcohol_tenor: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Heineken",
                "ibu": "4",
                "style": "Lager",
                "description": "Lager Premium",
                "alcohol_tenor": "5%"
            }
        }


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

    class Config:
        schema_extra = {
            "example": {
                "id": "1",
                "name": "Heineken",
                "ibu": "4",
                "style": "Lager",
                "description": "Lager Premium",
                "alcohol_tenor": "5%",
                "created_at": "2023-02-14 00:00:00",
                "updated_at": None,
            }
        }

