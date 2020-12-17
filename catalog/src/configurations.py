import os

from dataclasses import dataclass, fields as dataclasses_fields
from typing import Tuple

from catalog.src.exceptions import ConfigError

__all__ = [
    'get_config',
    'Config'
]


@dataclass
class Config:
    MONGO_HOST: str
    MONGO_PORT: str

    @classmethod
    def get_variables_names(cls) -> Tuple[str]:
        return tuple([str(field.name) for field in dataclasses_fields(cls)])


class EnvConfigRepository:

    def get(self) -> Config:
        missing_env_vars = self.__check_for_missing_vars()

        if len(missing_env_vars) > 0:
            raise ConfigError(f'Environment variables missing: {missing_env_vars}')

        config_dict = {}
        for env_var in Config.get_variables_names():
            config_dict[env_var] = os.environ[env_var]

        return Config(**config_dict)

    def __check_for_missing_vars(self):
        missing_env_vars = []
        for env_var in Config.get_variables_names():
            try:
                os.environ[env_var]
            except KeyError:
                missing_env_vars.append(env_var)
        return missing_env_vars


def get_config() -> Config:
    repository = EnvConfigRepository()
    config = repository.get()
    return config
