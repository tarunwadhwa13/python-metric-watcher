""" 
    Read from config and initialize 
"""
from metric_watcher.registry import Registry
from metric_watcher.config_store import CONFIG
from metric_watcher.reporters import BaseReporter
from metric_watcher.datastore import DBManager


class Singleton(object):
    _instances = {}

    def __new__(class_, *args, **kwargs):
        if class_ not in class_._instances:
            class_._instances[class_] = super(
                Singleton, class_).__new__(class_, *args, **kwargs)
        return class_._instances[class_]


class MetricWatcher(Singleton):
    def __init__(self):
        self._registry = Registry()
        # file path reference is used to ensure only one source if there for initialization
        DBManager.create_database(CONFIG.get('Common', {}).get('application', "Test"))

    def _initialize_from_config(self):
        # registering metrics
        for metric in CONFIG['Common']['metrics']:  # this is anyhow compulsory for us to supply metric onfo
            self.__register_metric(metric, CONFIG.get('Metrics', {}).get(metric, {}))

    def __set_reporter(self, reporter_dict):
        pass

    def __register_metric(self, metric, metric_info):
        manager = self._registry.add_metric(metric)

    def _deregister_reporter(self, reporter):
        pass

    def get_metric_manager(self, metric_name):
        if metric_name not in self._registry.metrics:
            raise LookupError(
                "No Metric Manager found for metric - %s" % (metric_name))
        return self._registry.metrics[metric_name]
