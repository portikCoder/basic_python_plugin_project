#  Copyright (c) 2021 portikCoder. All rights reserved.
#  See the license text under the root package.


import logging

from mainmodulename.common.config.config import Config
from mainmodulename.common.plugin_template import Plugin


class TypeOnePlugin(Plugin):
    """
    Plugin type ONE in
    """
    def __init__(self, config: Config):
        super().__init__(config)
        logging.info("Initialization")

    def run(self):
        logging.info("Doing a great job.")
