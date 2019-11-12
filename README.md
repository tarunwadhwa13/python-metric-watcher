1) Configparser integration with extended interpolation  https://docs.python.org/3/library/configparser.html#configparser.ExtendedInterpolation
   Current is .ini format. Will soon move to `toml` format once they start supporting interpolation

2) multiprocessing queue with ProcessPoolExecutor https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.get, https://docs.python.org/3.5/library/concurrent.futures.html

3) Registry to dump all data together

4) numpy to calculate percentiles


CORE Features
1) MetricManager - keeps track of tags, data for a particular METRIC. Guards entry of data into datastore for that particular metric.
2) Datastore - thread safe/process safe implementation of a data store. Stores till user defined retention period
3) Reporters - OpentsdbProxyReporter - to dump data to kafka in a format accepted by TSDB
4) Aggregator - triggers aggregator to aggregate data and return percentiles
5) Registry - Keeps track of overall metric managers, reporters etc
