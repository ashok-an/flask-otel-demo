run:
	python app.py 

otel:
	OTEL_RESOURCE_ATTRIBUTES=service.name=flask_app OTEL_EXPORTER_OTLP_ENDPOINT="http://localhost:4318"  opentelemetry-instrument --logs_exporter otlp_proto_http --traces_exporter otlp_proto_http --metrics_exporter otlp_proto_http python app.py

locust:
	locust -f locustfile.py --host http://127.0.0.1:8080 --users 100 --spawn-rate 2 --run-time 5m --headless --print-stats