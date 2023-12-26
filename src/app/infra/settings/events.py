import typing

import fastapi
import loguru

from app.infra.database.events_listens import dispose_db_connection, initialize_db_connection


def execute_app_server_event_handler(backend_app: fastapi.FastAPI) -> typing.Any:
    async def launch_backend_server_events() -> None:
        await initialize_db_connection(backend_app=backend_app)

    return launch_backend_server_events


def terminate_app_server_event_handler(backend_app: fastapi.FastAPI) -> typing.Any:
    @loguru.logger.catch
    async def stop_backend_server_events() -> None:
        await dispose_db_connection(backend_app=backend_app)

    return stop_backend_server_events
