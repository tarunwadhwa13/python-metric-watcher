"""
    Registry for managing metric data and functions.
    Responsible for communicating with datasource for adding, fetching data
    add action is thread safe as it uses queue to dump data and later pick from queue only
"""

from .metric_manager import MetricManager