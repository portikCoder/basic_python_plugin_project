#  Copyright (c) 2021 portikCoder. All rights reserved.
#  See the license text under the root package.
"""
Module's job is to have one thing done.
"""

from typing import Type

from mainmodulename.common.plugin_template import Plugin
from mainmodulename.plugins.type_one_plugin.type_one_plugin import TypeOnePlugin

PLUGIN_CLASS: Type[Plugin] = TypeOnePlugin
ALIASES = ["plugin-alias-one", "pluginaliasone", "plugin alias one"]


def get_plugin_class() -> Type[Plugin]:
    """
    If need some logic before returning the class itself purely, put it here.
    :return:
    """
    return PLUGIN_CLASS
