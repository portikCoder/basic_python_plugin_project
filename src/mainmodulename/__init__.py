#  Copyright (c) 2021 portikCoder. All rights reserved.
#  See the license text under the root package.

import logging

from mainmodulename.common.config.config import Config, ConfigFactory
from mainmodulename.common.config.limited_argument_parser import LimitedArgumentParser


def read_config() -> Config:

    argument_handler = get_argument_handler()
    config_path = argument_handler.config_path
    return ConfigFactory.factory(config_path)


def get_argument_handler() -> LimitedArgumentParser():
    argument_handler = LimitedArgumentParser()
    argument_handler.parse_arguments()
    return argument_handler


def init_loggers(logging_level: int):
    logging.getLogger().setLevel(logging_level)


def init_settings(config: Config):
    init_loggers(config.logging_level)
