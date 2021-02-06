#  Copyright (c) 2021 portikCoder. All rights reserved.
#  See the license text under the root package.
import logging
from abc import ABC
from typing import List

import toml

from mainmodulename.common.exceptions import BadConfigException


class Config(ABC):
    def __init__(self, file_path: str, logging_level: str = logging.getLevelName(logging.NOTSET)):
        self.logging_level = logging_level.upper()
        self.file_path = file_path


class PluginConfig(Config):
    def __init__(self, file_path: str, enabled_plugins: List[str], disabled_plugins: List[str], logging_level=None):
        super().__init__(file_path, logging_level)
        self.enabled_plugins = enabled_plugins
        self.disabled_plugins = disabled_plugins


class ConfigFactory:
    @staticmethod
    def factory(config_file_path: str):
        c_type = config_file_path.split('.')[-1].lower()

        if c_type == 'toml':
            config_reader = toml.load
            raw_config = ConfigFactory.load_raw_configfile(config_file_path, config_reader)
            logging_level = raw_config.get('logging_level', 'notset')
            enabled_plugins = raw_config.get('plugins').get('enable')
            disabled_plugins = raw_config.get('plugins').get('disable')
            file_path = raw_config.get('general').get('file')
            return PluginConfig(file_path, enabled_plugins, disabled_plugins, logging_level)
        else:
            raise BadConfigException("This type of config does not exist!")

    @staticmethod
    def load_raw_configfile(file_path: str, config_loader: any):
        try:
            with open(file_path, 'r') as f:
                config = config_loader(f)
            if not config:
                raise ValueError("Empty value for config!")
        except Exception as e:
            raise Exception(f"Failed to load config from {file_path} with '{type(config_loader)}'", e) from e
        return config
