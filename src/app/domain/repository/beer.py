import typing

import sqlalchemy
from sqlalchemy.sql import functions as sqlalchemy_functions

from app.crosscutting.exceptions.database import EntityDoesNotExist
from app.domain.models.beer import Beer
from app.domain.repository.base import BaseCRUDRepository
from app.domain.schemas.beer import BeerInCreate, BeerInUpdate


class BeerCRUDRepository(BaseCRUDRepository):
    async def create_beer(self, beer_create: BeerInCreate) -> Beer:
        new_beer = Beer(
            name=beer_create.name,
            ibu=beer_create.ibu,
            style=beer_create.style,
            description=beer_create.description,
            alcohol_tenor=beer_create.alcohol_tenor
        )

        self.async_session.add(instance=new_beer)
        await self.async_session.commit()
        await self.async_session.refresh(instance=new_beer)

        return new_beer

    async def read_beers(self) -> typing.Sequence[Beer]:
        stmt = sqlalchemy.select(Beer)
        query = await self.async_session.execute(statement=stmt)
        return query.scalars().all()

    async def read_beer_by_id(self, id: int) -> Beer:
        stmt = sqlalchemy.select(Beer).where(Beer.id == id)
        query = await self.async_session.execute(statement=stmt)

        if not query:
            raise EntityDoesNotExist("Account with id `{id}` does not exist!")

        return query.scalar()

    async def update_beer_by_id(self, id: int, beer_update: BeerInUpdate) -> Beer:
        new_beer_data = beer_update.dict()

        select_stmt = sqlalchemy.select(Beer).where(Beer.id == id)
        query = await self.async_session.execute(statement=select_stmt)
        update_beer = query.scalar()

        if not update_beer:
            raise EntityDoesNotExist(f"Beer with id `{id}` does not exist!")

        update_stmt = sqlalchemy.update(table=Beer).where(Beer.id == update_beer.id).values(updated_at=sqlalchemy_functions.now())

        if new_beer_data["name"]:
            update_stmt = update_stmt.values(name=new_beer_data["name"])
        if new_beer_data["ibu"]:
            update_stmt = update_stmt.values(ibu=new_beer_data["ibu"])
        if new_beer_data["style"]:
            update_stmt = update_stmt.values(style=new_beer_data["style"])
        if new_beer_data["description"]:
            update_stmt = update_stmt.values(description=new_beer_data["description"])
        if new_beer_data["alcohol_tenor"]:
            update_stmt = update_stmt.values(alcohol_tenor=new_beer_data["alcohol_tenor"])

        await self.async_session.execute(statement=update_stmt)
        await self.async_session.commit()
        await self.async_session.refresh(instance=update_beer)

        return update_beer

    async def delete_beer_by_id(self, id: int) -> str:
        select_stmt = sqlalchemy.select(Beer).where(Beer.id == id)
        query = await self.async_session.execute(statement=select_stmt)
        delete_beer = query.scalar()

        if not delete_beer:
            raise EntityDoesNotExist(f"Beer with id `{id}` does not exist!")

        stmt = sqlalchemy.delete(table=Beer).where(Beer.id == delete_beer.id)

        await self.async_session.execute(statement=stmt)
        await self.async_session.commit()

        return f"Beer with id '{id}' is successfully deleted!"
