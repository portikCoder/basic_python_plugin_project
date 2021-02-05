#  Copyright (c) 2021 portikCoder. All rights reserved.
#  See the license text under the root package.
from typing import Type

from mainmodulename.common.plugin_template import Plugin
from mainmodulename.plugins.type_one_plugin.type_one_plugin import TypeOnePlugin

PLUGIN_CLASS: Type[Plugin] = TypeOnePlugin
ALIASES = ['ctr', 'ctr_plugin', 'CtrFileNamePlugin']


def get_plugin_class() -> Type[Plugin]:
    """
    If need some logic before returning the class itself purely, put it here.
    :return:
    """
    return PLUGIN_CLASS
