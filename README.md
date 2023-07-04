# SabinoLabs

This repository is intended to be part of a reference architecture for microservices with FastAPI.

## Preconditions

* Python 3


## Clone the project

### Packaging as jar

```
git clone https://github.com/marciovrl/fastapi-example.git
```

### Run local

```
pip install -r requirements.txt
```

## Run server

```
uvicorn app.main:app --reload
```

## Run with docker

----

### Run server

```
docker-compose up -d --build
```


## API documentation (provided by Swagger UI)

```
http://127.0.0.1:8000/docs
```

### Run server
```
docker-compose exec db psql --username=fastapi --dbname=fastapi_dev
```

## Run with Kubernetes
```
make full-upgrade
```
