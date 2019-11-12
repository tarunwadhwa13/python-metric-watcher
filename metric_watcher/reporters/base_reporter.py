import threading

class BaseReporter:

    def schedule_reporting(self, interval):
        timer = threading.Timer(interval, self._collect_metric_data)
        timer.start()

    def _collect_metric_data(self):
        pass

    def _aggregate_data(self):
        pass

    def push_data(self):
        raise NotImplementedError("Reporter doesn't support pushing data")