from flask import Flask, Response  
import time
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter 
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader

# Setup OpenTelemetry Meter Provider
exporter = OTLPMetricExporter(endpoint="http://otel-collector:43200", insecure=True)
reader = PeriodicExportingMetricReader(exporter)
provider = MeterProvider(metric_readers=[reader])
metrics.set_meter_provider(provider)

# Create Meter
meter = metrics.get_meter_provider().get_meter("sample_flask_service")

# Create a counter metric
request_counter = meter.create_counter(
    name="http_requests",
    description="Counts the number of HTTP requests",
)

# Create Prometheus Counter
REQUEST_COUNT = Counter('http_requests_total', 'Counts the number of HTTP requests')

app = Flask(__name__)

@app.route("/")
def hello():
    request_counter.add(1)  # OpenTelemetry Metric
    REQUEST_COUNT.inc()  # Prometheus Metric
    return "Hello, OpenTelemetry!"

# Prometheus metrics endpoint
@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
