# coding=utf-8
import traceback

import os
import yaml
from pluginbase import PluginBase
from qutebrowser.plugins.plugin import Plugin

PLUGINS = {}


def load_plugins(objreg, parent, log):
    global PLUGINS
    log.init.debug("Initializing pluginbase...")
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    default_plugin_path = os.path.join(base_dir, 'plugins')

    log.init.debug("pluginbase path: {}".format(default_plugin_path))
    plugin_base = PluginBase(package="external_plugins")
    plugin_source = plugin_base.make_plugin_source(
        searchpath=[default_plugin_path])

    config = {"enabled": []}
    config_file_path = os.path.join(default_plugin_path, "config.yml")
    with open(config_file_path) as config_file:
        config = yaml.safe_load(config_file)
    if not isinstance(config, dict):
        raise AssertionError("config.yml must be a dict containing the key 'enabled'")
    if "enabled" not in config:
        raise AssertionError("config.yml must be a dict containing the key 'enabled'")

    for plugin_name in config["enabled"]:
        try:
            plugin_module = plugin_source.load_plugin(plugin_name)
            for attr_name in plugin_module.__dict__:
                if attr_name == 'Plugin':
                    continue
                attr = getattr(plugin_module, attr_name)
                try:
                    if not issubclass(attr, Plugin):
                        continue
                except TypeError:
                    continue
                plugin = attr(parent=parent)
                plugin._register()
                PLUGINS.update({plugin_name: plugin})
        except ModuleNotFoundError:
            traceback.print_exc()
            log.init.warning("Unable to load plugin: {}".format(plugin_name))
    log.init.debug("Loaded {} plugins: {}".format(
        len(PLUGINS), ', '.join([k for k in PLUGINS.keys()])))
