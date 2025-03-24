## Monitoring Setup

local setup includes: \
✅ Grafana for visualization\
✅ Prometheus for storing metrics\
✅ OpenTelemetry for collecting metrics

### Local Setup / Usage

To start the Monitoring containers:
```bash
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### View Metrics in Prometheus and Grafana
- Grafana: http://localhost:3000
- Add the following data sources:
  - Prometheus: http://prometheus:9090
  - Jaeger: http://jaeger:16686
- Access the endpoints from `otel-app`
  - http://localhost:31440/health
  - http://localhost:31440/random
  - http://localhost:31440/quote 
 
### otel-collector-config.yaml
- receivers.otlp: Allows the OpenTelemetry Collector to receive data from applications (OTLP over gRPC & HTTP).
- receivers.prometheus: Scrapes metrics from your sample app running on app:5000.
- processors.batch: Batches data to improve performance.
- exporters.prometheus: Exposes collected metrics at http://otel-collector:9464, where Prometheus can scrape them.
- exporters.otlp: (Optional) Sends telemetry data to another OTLP collector.
- service.pipelines.metrics: Defines the full flow of metrics from receivers → processors → exporters.
