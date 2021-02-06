#  Copyright (c) 2021 portikCoder. All rights reserved.
#  See the license text under the root package.
import logging

from mainmodulename.common.plugin_template import Plugin


class TypeOnePlugin(Plugin):
    def run(self):
        logging.info("Doing a great job.")
