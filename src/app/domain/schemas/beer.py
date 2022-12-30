from app.domain.schemas.base import BaseSchemaModel


class BeerBase(BaseSchemaModel):
    name: str
    ibu: int
    style: str
    description: str
    alcohol_tenor: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Heineken",
                "ibu": 19,
                "style": "Pale Lager",
                "description": "Pure Malt Lager",
                "alcohol_tenor": "5,0%"
            }
        }


class BeerInCreate(BeerBase):
    ...


class BeerInUpdate(BeerBase):
    ...
