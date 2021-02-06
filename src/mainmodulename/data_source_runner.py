#  Copyright (c) 2021 portikCoder. All rights reserved.
#  See the license text under the root package.
import logging
from typing import Type, Set

from mainmodulename.common.config.config import PluginConfig
from mainmodulename.common.plugin.plugin_loader import PluginLoader
from mainmodulename.common.plugin.plugin_module_type import PluginModuleType
from mainmodulename.common.plugin.plugin_template import Plugin


class PluginException(Exception):
    pass


class DataSourceRunner:
    def __init__(self, config: PluginConfig):
        self._config = config
        self._plugins: Set[PluginModuleType]

    def run(self):
        self._load_plugins()
        self._run_plugins()

    def _load_plugins(self):
        logging.info("Import plugins")
        import mainmodulename.plugins
        self._plugins = PluginLoader.get_avail_plugins_from(mainmodulename.plugins, disable_plugins = set(self._config.enabled_plugins) -set(self._config.disabled_plugins))
        logging.info("Filter plugins")
        self._plugins = set(filter(lambda
                                       plugin: plugin[0] if plugin[1] in self._config.enabled_plugins and plugin[1] not in self._config.disabled_plugins else None,
                                   [(x.PLUGIN_CLASS,y) for x in self._plugins for y in x.ALIASES]))
        logging.info("Import plugins is done")
        logging.debug(f"Avail plugins are: {self._plugins}")

    def _run_plugins(self):
        if not self._plugins:
            raise PluginException("There is no plugin loaded!")

        logging.info("Run plugins")
        for plugin_module in self._plugins:
            plugin_class: Type[Plugin] = plugin_module.get_plugin_class()
            plugin = plugin_class(config=self._config)
            plugin.run()
        logging.info("Run plugins is done")
