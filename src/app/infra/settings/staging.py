from app.infra.settings.base import AppBaseSettings
from app.infra.settings.environment import Environment


class BackendStageSettings(AppBaseSettings):
    DESCRIPTION: str | None = "Test Environment."
    DEBUG: bool = True
    ENVIRONMENT: Environment = Environment.STAGING
