import fastapi
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from starlette_prometheus import metrics, PrometheusMiddleware

from app.api.api_v1.api import api_router
from app.infra.settings.manager import settings
from app.infra.settings.events import execute_app_server_event_handler, terminate_app_server_event_handler


def initialize_application() -> fastapi.FastAPI:
    app = fastapi.FastAPI(**settings.set_app_attributes)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=settings.IS_ALLOWED_CREDENTIALS,
        allow_methods=settings.ALLOWED_METHODS,
        allow_headers=settings.ALLOWED_HEADERS,
    )

    app.add_event_handler(
        "startup",
        execute_app_server_event_handler(backend_app=app),
    )
    app.add_event_handler(
        "shutdown",
        terminate_app_server_event_handler(backend_app=app),
    )

    app.include_router(router=api_router, prefix=settings.API_PREFIX)
    app.add_middleware(PrometheusMiddleware)
    app.add_route("/metrics", metrics)

    return app


beer_app: fastapi.FastAPI = initialize_application()

if __name__ == "__main__":
    uvicorn.run(
        app="main:beer_app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.DEBUG,
        workers=settings.SERVER_WORKERS,
        log_level=settings.LOGGING_LEVEL,
    )
