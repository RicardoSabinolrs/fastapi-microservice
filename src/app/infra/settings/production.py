from app.infra.settings.base import AppBaseSettings
from app.infra.settings.environment import Environment


class BackendProdSettings(AppBaseSettings):
    DESCRIPTION: str | None = "Production Environment."
    ENVIRONMENT: Environment = Environment.PRODUCTION
