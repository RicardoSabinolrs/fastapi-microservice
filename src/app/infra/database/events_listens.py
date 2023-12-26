import fastapi
import loguru
from sqlalchemy import event
from sqlalchemy.dialects.postgresql.asyncpg import AsyncAdapt_asyncpg_connection
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.pool.base import _ConnectionRecord

from app.infra.database.async_session import async_db
from app.infra.database.metadata_orm import Base


@event.listens_for(target=async_db.async_engine.sync_engine, identifier="connect")
def inspect_db_server_on_connection(
        db_api_connection: AsyncAdapt_asyncpg_connection, connection_record: _ConnectionRecord
) -> None:
    loguru.logger.debug(f"New DB API Connection ---\n {db_api_connection}")
    loguru.logger.debug(f"Connection Record ---\n {connection_record}")


@event.listens_for(target=async_db.async_engine.sync_engine, identifier="close")
def inspect_db_server_on_close(
        db_api_connection: AsyncAdapt_asyncpg_connection, connection_record: _ConnectionRecord
) -> None:
    loguru.logger.debug(f"Closing DB API Connection ---\n {db_api_connection}")
    loguru.logger.debug(f"Closed Connection Record ---\n {connection_record}")


async def initialize_db_tables(connection: AsyncConnection) -> None:
    loguru.logger.debug("Database Table Creation --- Initializing . . .")

    await connection.run_sync(Base.metadata.create_all)

    loguru.logger.debug("Database Table Creation --- Successfully Initialized!")


async def initialize_db_connection(backend_app: fastapi.FastAPI) -> None:
    loguru.logger.debug("Database Connection --- Establishing . . .")

    backend_app.state.db = async_db

    # async with backend_app.state.db.async_engine.begin() as connection:
    #     await initialize_db_tables(connection=connection)

    loguru.logger.debug("Database Connection --- Successfully Established!")


async def dispose_db_connection(backend_app: fastapi.FastAPI) -> None:
    loguru.logger.debug("Database Connection --- Disposing . . .")

    await backend_app.state.db.async_engine.dispose()

    loguru.logger.debug("Database Connection --- Successfully Disposed!")
