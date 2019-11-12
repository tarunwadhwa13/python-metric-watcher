""" 
	Load config from file and create a dictionary like object for handling configs across module
"""

from configparser import ConfigParser, ExtendedInterpolation
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILE_NAME = os.environ.get("METRIC_WATCHER_CONF_FILE", os.path.join(BASE_DIR, "watcher.conf"))

def parse_config():
    # function to abstract loading logic and make module faster
    if not os.path.exists(FILE_NAME) or not os.path.isfile(FILE_NAME):
        raise LookupError("""
                Valid config file wasn't found on path defined. 
                Please use 'METRIC_WATCHER_CONF_FILE' to set correct path of config file
            """)
    _config = ConfigParser(interpolation=ExtendedInterpolation())
    _config.read(FILE_NAME)
    return _config

CONFIG = parse_config()
CONFIG['Common']['BASE_DIR'] = BASE_DIR
