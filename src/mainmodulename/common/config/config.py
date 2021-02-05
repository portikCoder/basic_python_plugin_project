#  Copyright (c) 2021 portikCoder. All rights reserved.
#  See the license text under the root package.
import logging

from abc import ABC


class Config(ABC):
    def __init__(self, logging_level: int = logging.NOTSET):
        self.logging_level = logging_level
