#  Copyright (c) 2021 portikCoder. All rights reserved.
#  See the license text under the root package.
import types
from abc import abstractmethod
from typing import List, Type

from mainmodulename.common.plugin.plugin_template import Plugin


class PluginModuleType(types.ModuleType):
    PLUGIN_CLASS: object = ...
    ALIASES: List[str] = ...  # only for d-source plugins are needed

    @abstractmethod
    def get_plugin_class(self) -> Type[Plugin]: pass
