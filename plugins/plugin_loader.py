import importlib.util
import os

def load_plugins(plugin_folder):
    plugins = []
    for filename in os.listdir(plugin_folder):
        if filename.endswith(".py"):
            spec = importlib.util.spec_from_file_location(filename[:-3], os.path.join(plugin_folder, filename))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            plugins.append(module)
    return plugins