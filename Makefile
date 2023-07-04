API=$(shell kubectl get pod -n beer-api -l component=beer-api -o jsonpath="{.items[0].metadata.name}")

full-upgrade: push-image upgrade

upgrade:
	kubectl apply -f kubernetes/manifests/namespace.yaml -n beer-api; \
	kubectl apply -f kubernetes/manifests/configmap.yaml -n beer-api; \
	kubectl apply -f kubernetes/manifests/secret.yaml -n beer-api; \
	kubectl apply -f kubernetes/manifests/deployment.yaml -n beer-api; \
	kubectl apply -f kubernetes/manifests/service.yaml -n beer-api; \
	kubectl apply -f kubernetes/manifests/ingress.yaml -n beer-api; \
	kubectl apply -f kubernetes/manifests/hpa.yaml -n beer-api

build:
	docker build . -t sabinolabs/beer-api:latest

push-image: build
	docker push sabinolabs/beer-api:latest

registry-login:
	docker login

tunnel:
	kubectl port-forward $(API) -n beer-api 8000:8000

local-test-with-minikube: docker-daemon-minikube
	docker-compose -f docker-compose.local.yml up --build

docker-daemon-local:
	eval $(minikube docker-env -u)

docker-daemon-minikube:
	eval $(minikube docker-env)