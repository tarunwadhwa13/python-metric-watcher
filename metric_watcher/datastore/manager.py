"""
    Using sqlite only to use its transactional and atomic capabilities.
    Building own datastructure for this would be an overhead
"""

import inspect
import os
import sqlite3
import hashlib

from schema import Schema, And
from metric_watcher.datastore import queries
from metric_watcher.config_store import CONFIG


class DBManager:

    DB_PATH = None
    INPUT_SCHEMA = Schema({
        "index": str,
        "tags": And(dict, len)
    })
    DB_CONN = None

    @classmethod
    def _get_connection(cls):
        if not DBManager.DB_CONN:
            DBManager.DB_CONN = sqlite3.connect(DBManager.DB_PATH)
        return DBManager.DB_CONN

    @classmethod
    def create_database(cls, app_name):

        # ensure database is initialized from one source only
        # caller_function = inspect.getouterframes(inspect.currentframe(), 2)
        # print(caller_function)
        # assert caller_function[1][1] == "metric_watcher/__init__.py", "Datastore can be initialized by MetricWather class only"

        DBManager.DB_PATH = os.path.join(
            CONFIG['Common']['BASE_DIR'], app_name) + ".db"

        # delete db if already exists
        if os.path.exists(DBManager.DB_PATH):
            os.remove(DBManager.DB_PATH)

        # create database
        sqlite3.connect(DBManager.DB_PATH)

    @classmethod
    def setup_metric_sink(cls, metric):
        metric = metric.encode('utf-8')
        metric_hash = hashlib.sha224(metric).hexdigest()
        connection = DBManager._get_connection()
        connection.execute(queries.CREATE_METRIC_SINK.format(
            table_name=str(metric_hash)))
        connection.execute(queries.CREATE_AGGREGATED_DATA_TABLE.format(
            table_name=f'{metric_hash}-aggregated'))
        return metric_hash

    @classmethod
    def validate_data_format(cls, data):
        pass

    @classmethod
    def push_data(cls, index, data):
        cls.validate_data_format(data)
        pass

    @classmethod
    def get_data(cls, index, start_time, end_time):
        connection = DBManager._get_connection()
        query = queries.GET_METRIC_DATA_FOR_INTERVAL.format(
            table_name=index
        )
        print(query)
        db_output = connection.execute(query, (start_time, end_time))
        return db_output.fetchall()
