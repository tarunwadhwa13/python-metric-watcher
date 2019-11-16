from metric_watcher.datastore import DBManager

class MetricManager:
    """ Manages attributes like timers, reporters for a metric """

    def __init__(self, metric):
        self.metric = metric
        self.reporters = {}
        self.timers = {}
        self.datasource_index = self._initialize_database(self.metric)
    
    def _initialize_database(self, metric):
        index_id = DBManager.setup_metric_sink(metric=metric)
        return index_id

    def get_metric_data(self, start_time, end_time):
        metric_data = DBManager.get_data(self.datasource_index, start_time, end_time)
        return metric_data

    def add_data(self, value, tags):
        # untagged data for a metric should not be allowed
        assert tags, "Untagged data is not allowed"
        assert isinstance(tags, dict), "Tags must be dict"
