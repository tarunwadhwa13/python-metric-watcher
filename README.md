## Python Metric Watcher

This module will eventually profile code and measure runtime stats of your python program.
Metrics collected can be aggregated and pushed to external system

Key Components
1) MetricManager - keeps track of tags, data for a particular METRIC. Guards entry of data into datastore for that particular metric.
2) Datastore - uses sqlite as backend for now to ensure atomicity and transactional behavior.
3) Aggregator - aggregates data (percentiles and average) and stores it separately
4) Reporters - can be used to report metric aggregated data to an external system
5) Registry - Keeps track of overall metric managers, reporters etc

