#  Copyright (c) 2021 portikCoder. All rights reserved.
#  See the license text under the root package.
import argparse


class LimitedArgumentParser():
    """
    The class is responsible for handling all the command line options safely.
    """

    def __init__(self):
        self._parser = argparse.ArgumentParser(
            description='This will handle all the required field needed for the tool\'s run.')
        #   Required - fields goes here
        self._parser.add_argument('-c', '--config_path', help='Config file path (absolute or relative)', type=str,
                                  required=True)
        #   NON-Required - fields goes here
        self._parser.add_argument('-da', '--debug_mode_active', help='If you want to log in debug mode',
                                  action='store_true', required=False)
        self._parser.add_argument('-t', '--test_mode', help='If you want to test the app',
                                  action='store_true', required=False)
        self.arguments = argparse.ArgumentParser

    def parse_arguments(self):
        self.arguments = self._parser.parse_args()

    @property
    def config_path(self):
        config_path = 'config_path'
        return getattr(self.arguments, config_path)
