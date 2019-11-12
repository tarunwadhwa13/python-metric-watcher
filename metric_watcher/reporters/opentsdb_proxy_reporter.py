from .base_reporter import BaseReporter
from datetime import datetime


class OpenTSDBProxyReporter(BaseReporter):
    def __init__(self):
        self.last_push = None

    def push_data(self):
        pass