#  Copyright (c) 2021 portikCoder. All rights reserved.
#  See the license text under the root package.
import logging

from mainmodulename import read_config, init_settings
from mainmodulename.common.config.config import Config
from mainmodulename.data_source_runner import DataSourceRunner


def main():
    config: Config = read_config()
    config.logging_level = logging.DEBUG
    init_settings(config)
    logging.info("Setup is done")
    logging.info("Prepare plugins to be run")
    DataSourceRunner(config).run()


if __name__ == '__main__':
    main()
