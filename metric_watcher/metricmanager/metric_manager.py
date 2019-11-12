from metric_watcher.datastore import DBManager
import hashlib

class MetricManager:
    """ Manages attributes like timers, reporters for a metric """

    def __init__(self, metric):
        self.metric = metric
        self._reporters = {}
        self._timers = {}
        self._datasource_index = self._initialize_database(self.metric)
    
    def _initialize_database(self, metric):
        return hashlib.sha224(metric).hexdigest()

    def reporters(self):
        # getter for reporters
        return self._reporters

    def get_metric_data(self, start_time, end_time, downsample=0):
        pass

    def add_data(self, value, tags):
        # untagged data for a metric should not be allowed
        assert tags, "Untagged data is not allowed"
        assert isinstance(tags, dict), "Tags must be dict"




