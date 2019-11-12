""" 
    Reporters can periodically notify/push data . 
    This module abstracts working of reporters. 
    Reporters are configured using section starting with Reporters.*
    Reporting composite metrics is not supported as of now so you need to create one reporter for every metric
    Hence there can be multiple reporters for same metric but no reporter can report multiple metrics
"""

from .opentsdb_proxy_reporter import OpenTSDBProxyReporter
from .base_reporter import BaseReporter