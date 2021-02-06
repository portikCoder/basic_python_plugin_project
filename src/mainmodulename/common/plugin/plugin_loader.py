#  Copyright (c) 2021 portikCoder. All rights reserved.
#  See the license text under the root package.
import pkgutil

import importlib
from types import ModuleType
from typing import Set

from mainmodulename.common.plugin.plugin_module_type import PluginModuleType


class PluginLoader(object):
    @classmethod
    def get_avail_plugins_from(cls, plugin_namespace, disable_plugins:Set = ()) -> Set[PluginModuleType]:
        # TODO: use up .ALIASES with disable set wisely
        return {
            importlib.import_module(module_name)
            for _, module_name, _
            in cls.iter_namespace(plugin_namespace) if module_name
        }

    @classmethod
    def iter_namespace(cls, plugin_namespace: ModuleType):
        return pkgutil.iter_modules(plugin_namespace.__path__, plugin_namespace.__name__ + ".")
