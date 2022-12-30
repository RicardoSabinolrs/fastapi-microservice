from app.infra.settings.base import AppBaseSettings
from app.infra.settings.environment import Environment


class BackendDevSettings(AppBaseSettings):
    DESCRIPTION: str | None = "Development Environment."
    DEBUG: bool = True
    ENVIRONMENT: Environment = Environment.DEVELOPMENT
