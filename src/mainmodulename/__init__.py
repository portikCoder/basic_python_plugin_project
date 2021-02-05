#  Copyright (c) 2021 portikCoder. All rights reserved.
#  See the license text under the root package.
import logging

from mainmodulename.common.config.config import Config


def read_config() -> Config:
    return Config()


def init_loggers(logging_level: int):
    logging.getLogger().setLevel(logging_level)


def init_settings(config: Config):
    init_loggers(config.logging_level)
