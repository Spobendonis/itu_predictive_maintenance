from prometheus_client import start_http_server, Summary, Gauge, Counter, MetricsHandler
import random
import time


def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    g = Gauge('harddrive_health', 'Health of harddrive', ['id'])
    # Start up the server to expose the metrics.
    start_http_server(8003)
    while True:
        process_request(random.random())
        g.labels(id='1234').inc()      # Increment by 1
        g.labels(id='1235').inc()