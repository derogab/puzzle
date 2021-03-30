import inspect
import os
import pkgutil
import logging
import time

from threading import Thread

# Init logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


class Plugin(Thread):
    """ Base class that each plugin must inherit from. within this class
    you must define the methods that all of your plugins must implement 
    """

    def __init__(self):
        Thread.__init__(self)
        self.description = 'UNKNOWN'
        self.tools = None

    def set_tools(self, tools):
        """ The method to provide the main tools for plugins """
        self.tools = tools

    def run(self):
        """ The method that we expect all plugins to implement. This is the
        method that our framework will call 
        """
        raise NotImplementedError


class PluginCollection(object):
    """ Upon creation, this class will read the plugins package for modules
    that contain a class definition that is inheriting from the Plugin class
    """

    def __init__(self, plugin_package, tools):
        """ Constructor that initiates the reading of all available plugins
        when an instance of the PluginCollection object is created
        """
        self.plugin_package = plugin_package
        self.reload_plugins()
        self.tools = tools


    def reload_plugins(self):
        """ Reset the list of all plugins and initiate the walk over the main
        provided plugin package to load all available plugins
        """
        self.plugins = []
        self.seen_paths = []
        logging.info('Looking for plugins under package ' + self.plugin_package)
        self.walk_package(self.plugin_package)


    def start_all_plugins(self):
        """ Start all of the plugins as threads """
        logging.info('Starting all plugins...')
        for plugin in self.plugins:
            # Set tools
            plugin.set_tools(self.tools)
            # Start the plugin as thread
            logging.info('Start Plugin ' + plugin.description)
            plugin.start()

    def walk_package(self, package):
        """ Recursively walk the supplied package to retrieve all plugins """
        imported_package = __import__(package, fromlist=['blah'])

        for _, pluginname, ispkg in pkgutil.iter_modules(imported_package.__path__, imported_package.__name__ + '.'):
            if not ispkg:
                plugin_module = __import__(pluginname, fromlist=['blah'])
                clsmembers = inspect.getmembers(plugin_module, inspect.isclass)
                for (_, c) in clsmembers:
                    # Only add classes that are a sub class of Plugin, but NOT Plugin itself
                    if issubclass(c, Plugin) & (c is not Plugin):
                        logging.info('Found plugin class' + c.__module__ + '.' + c.__name__)
                        self.plugins.append(c())


        # Now that we have looked at all the modules in the current package, start looking
        # recursively for additional modules in sub packages
        all_current_paths = []
        if isinstance(imported_package.__path__, str):
            all_current_paths.append(imported_package.__path__)
        else:
            all_current_paths.extend([x for x in imported_package.__path__])

        for pkg_path in all_current_paths:
            if pkg_path not in self.seen_paths:
                self.seen_paths.append(pkg_path)

                # Get all sub directory of the current package path directory
                child_pkgs = [p for p in os.listdir(pkg_path) if os.path.isdir(os.path.join(pkg_path, p))]

                # For each sub directory, apply the walk_package method recursively
                for child_pkg in child_pkgs:
                    self.walk_package(package + '.' + child_pkg)
