import typing

from sqlalchemy.ext.asyncio import (
    AsyncSession as SQLAlchemyAsyncSession,
)

from app.infra.database.async_engine_postgresql import async_db


async def get_async_session() -> typing.AsyncGenerator[SQLAlchemyAsyncSession, None]:
    async_session_maker = async_db.create_async_session()
    async_session = async_session_maker()

    try:
        yield async_session
    except Exception as e:
        print(e)
        await async_session.rollback()
    finally:
        await async_session.close()
