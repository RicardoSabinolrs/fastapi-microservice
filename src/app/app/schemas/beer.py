from pydantic import BaseModel


class BeerBase(BaseModel):
    id: int
    name: str
    ibu: int
    style: str
    description: str
    alcohol_tenor: str

    class Config:
        orm_mode = True


# Properties to receive via API on creation
class BeerCreate(BaseModel):
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


# Properties to receive via API on update
class BeerUpdate(BeerBase):
    ...


# Additional properties to return via API
class Beer(BeerBase):
    ...
