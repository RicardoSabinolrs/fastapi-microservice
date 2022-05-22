API=$(shell kubectl get pod -n beer-api -l component=beer-api -o jsonpath="{.items[0].metadata.name}")

full-upgrade: push-image upgrade

upgrade:
	kubectl apply -f manifests/configmap.yaml -n motorist-api; \
	kubectl apply -f manifests/secret.yaml -n motorist-api; \
	kubectl apply -f manifests/deployment.yaml -n motorist-api; \
	kubectl apply -f manifests/service.yaml -n motorist-api; \
	kubectl apply -f manifests/ingress.yaml -n motorist-api
	kubectl apply -f manifests/hpa.yaml -n motorist-api


build:
	docker build . -t sabinolabs/beer-api:latest -f src/Dockerfile

push-image: build
	docker push sabinolabs/beer-api:latest

registry-login:
	docker login

tunnel:
	kubectl port-forward $(API) -n beer-api 8001:8001

local-test:
	docker-compose -f docker-compose.local.yml up --build