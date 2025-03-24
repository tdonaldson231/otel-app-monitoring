# OTEL App

## Build and Run the Docker Image
```
docker build -t otel-app:latest .
```

## Deploy to Kubernetes (running locally using Docker Desktop)
### Apply the Kubernetes configuration
```
kubectl apply -f k8s-deployment.yaml
```

### Check if the pod is running
```
kubectl get pods
```

### Check the Service and NodePort
```
kubectl get svc otel-app-service
```

#### Example
```
$ kubectl get svc otel-app-service
NAME               TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
otel-app-service   NodePort   10.96.200.162   <none>        80:31205/TCP   33m
```

### Access the App
```
http://localhost:31234/health
http://localhost:31234/random
http://localhost:31234/quote
```

#### Port-Forward as an Alternative
If you want a quicker way to access the app without a NodePort, you can use `kubectl port-forward`:
```
kubectl port-forward deployment/otel-app 8080:8080
http://localhost:8080/health
```

## Grafana
Refer to `grafana` directory for setup instructions to view open telemetry data from grafana.