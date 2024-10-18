# kas - setup tool for bitbake based projects
#
# Copyright (c) Siemens AG, 2017-2018
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
    This module contains and manages kas plugins
"""

import importlib
import os
import semantic_version as sv

PLUGINS = {}


def register_plugins(mod, kasver):
    """
        Register all kas plugins found in a module
    """
    min = getattr(mod, '__KAS_MIN__')
    max = getattr(mod, '__KAS_MAX__')
    for plugin in getattr(mod, '__KAS_PLUGINS__', []):
        if sv.Version.coerce(min) <= sv.Version.coerce(kasver) and \
                sv.Version.coerce(kasver) <= sv.Version.coerce(max):
            PLUGINS[plugin.name] = plugin
        else:
            print(f'Ignoring plugin {plugin.name} - version mismatch')



def load(kasver):
    """
        Import all kas plugins
    """
    plugins_dir = os.path.dirname(__file__)
    for filename in os.listdir(plugins_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            plugin_name = filename[:-3]
            module = importlib.import_module(f".{plugin_name}", package=__package__)
            register_plugins(module, kasver)

def get(name):
    """
        Lookup a kas plugin class by name
    """
    return PLUGINS.get(name, None)


def all():
    """
        Get a list of all loaded kas plugin classes
    """
    return PLUGINS.values()
