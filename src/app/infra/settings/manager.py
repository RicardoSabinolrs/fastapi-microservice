from functools import lru_cache

import decouple

from app.infra.settings.base import AppBaseSettings
from app.infra.settings.development import BackendDevSettings
from app.infra.settings.environment import Environment
from app.infra.settings.production import BackendProdSettings
from app.infra.settings.staging import BackendStageSettings


class BackendSettingsFactory:
    def __init__(self, environment: str):
        self.environment = environment

    def __call__(self) -> AppBaseSettings:
        if self.environment == Environment.DEVELOPMENT.value:
            return BackendDevSettings()
        elif self.environment == Environment.STAGING.value:
            return BackendStageSettings()
        return BackendProdSettings()


@lru_cache()
def get_settings() -> AppBaseSettings:
    return BackendSettingsFactory(environment=decouple.config("ENVIRONMENT", default="DEV", cast=str))()  # type: ignore


settings: AppBaseSettings = get_settings()
