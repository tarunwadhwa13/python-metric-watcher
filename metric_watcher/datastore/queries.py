"""
    Contains prepared statement for sqlite. 
    Table name cannot be dynamic hence need to be substituted in python itself
"""

# table for keeping metric data
CREATE_METRIC_SINK = "Create table '{table_name}' (timestamp TIMESTAMP PRIMARY KEY DEFAULT CURRENT_TIMESTAMP, tags TEXT)"

# table for keeping aggregated data
CREATE_AGGREGATED_DATA_TABLE = "Create table '{table_name}' (dimension VARCHAR(50), tags TEXT, aggregated_at TIMESTAMP)"

# get data from table
GET_METRIC_DATA_FOR_INTERVAL = "Select * from '{table_name}' where timestamp between ? and ?"
