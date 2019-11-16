import os

import toml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILE_NAME = os.environ.get("METRIC_WATCHER_CONF_FILE",
                           os.path.join(BASE_DIR, "watcher.conf"))


def get_config_content():
    if not os.path.exists(FILE_NAME) or not os.path.isfile(FILE_NAME):
        raise LookupError("""
                Valid config file wasn't found on path defined.
                Please use 'METRIC_WATCHER_CONF_FILE' to set correct path of config file
            """)
    _config = toml.load(FILE_NAME)
    return _config


def run_config_test(CONFIG):
    # metric info available test
    for metric in CONFIG['Common']['metrics']:
        assert f'{metric}' in CONFIG['Metrics'], f'No such section Metric."{metric}" available for - {metric}'
    # reporter available test


CONFIG = get_config_content()
CONFIG['Common']['BASE_DIR'] = BASE_DIR
print(CONFIG)
run_config_test(CONFIG)
