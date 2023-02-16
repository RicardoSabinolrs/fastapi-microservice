import logging
import pathlib

import decouple
import pydantic

ROOT_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent.parent.parent.parent.resolve()


class AppBaseSettings(pydantic.BaseSettings):
    TITLE: str = "Sabino -|Labs Microservice Rest Template with FastAPI"
    VERSION: str = "0.1.0"
    TIMEZONE: str = "UTC"
    DESCRIPTION: str | None = None
    DEBUG: bool = False

    SERVER_HOST: str = decouple.config("BACKEND_SERVER_HOST", cast=str)
    SERVER_PORT: int = decouple.config("BACKEND_SERVER_PORT", cast=int)
    SERVER_WORKERS: int = decouple.config("BACKEND_SERVER_WORKERS", cast=int)
    API_PREFIX: str = "/api"
    DOCS_URL: str = "/docs"
    OPENAPI_URL: str = "/openapi.json"
    REDOC_URL: str = "/redoc"
    OPENAPI_PREFIX: str = ""

    DB_POSTGRES_HOST: str = decouple.config("POSTGRES_HOST", cast=str)
    DB_MAX_POOL_CON: int = decouple.config("DB_MAX_POOL_CON", cast=int, default=80)
    DB_POSTGRES_NAME: str = decouple.config("POSTGRES_DB", cast=str)
    DB_POSTGRES_PASSWORD: str = decouple.config("POSTGRES_PASSWORD", cast=str)
    DB_POOL_SIZE: int = decouple.config("DB_POOL_SIZE", cast=int, default=100)
    DB_POOL_OVERFLOW: int = decouple.config("DB_POOL_OVERFLOW", cast=int, default=20)
    DB_POSTGRES_PORT: int = decouple.config("POSTGRES_PORT", cast=int)
    DB_POSTGRES_SCHEMA: str = decouple.config("POSTGRES_SCHEMA", cast=str)
    DB_TIMEOUT: int = decouple.config("DB_TIMEOUT", cast=int, default=5)
    DB_POSTGRES_USERNAME: str = decouple.config("POSTGRES_USER", cast=str)

    IS_DB_ECHO_LOG: bool = decouple.config("IS_DB_ECHO_LOG", cast=bool)
    IS_DB_FORCE_ROLLBACK: bool = decouple.config("IS_DB_FORCE_ROLLBACK", cast=bool)
    IS_DB_EXPIRE_ON_COMMIT: bool = decouple.config("IS_DB_EXPIRE_ON_COMMIT", cast=bool)

    API_TOKEN: str = decouple.config("API_TOKEN", cast=str, default='1232')
    AUTH_TOKEN: str = decouple.config("AUTH_TOKEN", cast=str, default='1233')
    JWT_TOKEN_PREFIX: str = decouple.config("JWT_TOKEN_PREFIX", cast=str)
    JWT_SECRET_KEY: str = decouple.config("JWT_SECRET_KEY", cast=str)
    JWT_SUBJECT: str = decouple.config("JWT_SUBJECT", cast=str)
    JWT_MIN: int = decouple.config("JWT_MIN", cast=int)
    JWT_HOUR: int = decouple.config("JWT_HOUR", cast=int)
    JWT_DAY: int = decouple.config("JWT_DAY", cast=int)
    JWT_ACCESS_TOKEN_EXPIRATION_TIME: int = JWT_MIN * JWT_HOUR * JWT_DAY

    IS_ALLOWED_CREDENTIALS: bool = decouple.config("IS_ALLOWED_CREDENTIALS", cast=bool)
    ALLOWED_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://0.0.0.0:3000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3001",
        "http://localhost:5173",
        "http://0.0.0.0:5173",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
    ]
    ALLOWED_METHODS: list[str] = ["*"]
    ALLOWED_HEADERS: list[str] = ["*"]

    LOGGING_LEVEL: int = logging.INFO
    LOGGERS: tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    HASHING_ALGORITHM_LAYER_1: str = decouple.config("HASHING_ALGORITHM_LAYER_1", cast=str)
    HASHING_ALGORITHM_LAYER_2: str = decouple.config("HASHING_ALGORITHM_LAYER_2", cast=str)
    HASHING_SALT: str = decouple.config("HASHING_SALT", cast=str)
    JWT_ALGORITHM: str = decouple.config("JWT_ALGORITHM", cast=str)

    class Config(pydantic.BaseConfig):
        case_sensitive: bool = True
        env_file: str = f"{str(ROOT_DIR)}/.env"
        validate_assignment: bool = True

    @property
    def set_app_attributes(self) -> dict[str, str | bool | None]:
        """
        Set all `FastAPI` class' attributes with the custom values defined in `AppBaseSettings`.
        """
        return {
            "title": self.TITLE,
            "version": self.VERSION,
            "debug": self.DEBUG,
            "description": self.DESCRIPTION,
            "docs_url": self.DOCS_URL,
            "openapi_url": self.OPENAPI_URL,
            "redoc_url": self.REDOC_URL,
            "openapi_prefix": self.OPENAPI_PREFIX,
            "api_prefix": self.API_PREFIX,
        }
