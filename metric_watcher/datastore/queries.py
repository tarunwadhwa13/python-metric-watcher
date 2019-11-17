"""
    Contains prepared statement for sqlite. 
    Table name cannot be dynamic hence need to be substituted in python itself
"""

# table for keeping metric data
CREATE_METRIC_DATA_TABLE = "Create table '{table_name}' (timestamp TIMESTAMP PRIMARY KEY DEFAULT CURRENT_TIMESTAMP, value INTEGER, tags TEXT)"

# table for keeping aggregated data
CREATE_AGGREGATED_DATA_TABLE = "Create table '{table_name}' (dimension VARCHAR(50), value INTEGER, tags TEXT, aggregated_at TIMESTAMP)"

# get data from table
GET_METRIC_DATA_FOR_INTERVAL = "Select * from '{table_name}' where timestamp between ? and ?"

# push data for a metric
PUSH_METRIC_DATA = "Insert into '{table_name}' (value, tags) values (?, ?)"