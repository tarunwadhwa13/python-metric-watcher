from metric_watcher.metricmanager import MetricManager

class Registry:
    
    def __init__(self):
        self.metrics = {}  # keep metric managers per metric 
        self.reporters = {}  # keeps reporters and linked metrics
    

    def add_metric(self, metric):
        manager = MetricManager(metric)
        self.metrics[metric] = manager
        return manager
        