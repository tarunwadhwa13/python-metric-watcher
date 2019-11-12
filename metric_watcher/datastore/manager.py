"""
    Using sqlite only to use its transactional and atomic capabilities.
    Building own datastructure for this would be an overhead
"""

import sqlite3
import os
from metric_watcher.config_store import CONFIG
import inspect

class DBManager:
    def __init__(self, app_name):
        caller_function = inspect.getouterframes(inspect.currentframe(), 2)
        assert caller_function[1][1] == "metric_watcher/__init__.py", "Datastore can be initialized by MetricWather class only"
        self.db_path = os.path.join(CONFIG['Common']['BASE_DIR'], app_name) + ".db"
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        sqlite3.connect(self.db_path)
