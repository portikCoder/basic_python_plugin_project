#  Copyright (c) 2021 portikCoder. All rights reserved.
#  See the license text under the root package.
from abc import ABC, abstractmethod

from mainmodulename import Config


class Plugin(ABC):
    """
    For giving the base structure guidelines.

    Getting :py:meth:`plugin_module_type.PluginModuleType.get_plugin_class` has a unique working method.
    First it returns the actual worker-class which does the job needed.
    Therefore it must be instantiated firstly, then call its :func:`ReportCalculatorPlugin.run` method which may or may not return anything.
    """

    def __init__(self, config: Config):
        self.config = config

    @abstractmethod
    def run(self):
        """
        Implement the logic in this function, because this is the one which will be called trough runtime.
        :return:
        """
        pass
