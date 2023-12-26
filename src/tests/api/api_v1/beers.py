# tests/test_beer.py
import json
from unittest.mock import MagicMock

from src.main import beer_app
from fastapi.testclient import TestClient

from app.domain.repository.beer import BeerCRUDRepository

client = TestClient(beer_app)


def test_create_beer(mocker):
    # Dados de teste
    new_beer_data = {
        "name": "Test Beer",
        "ibu": 30,
        "style": "Test Style",
        "description": "Test Description",
        "alcohol_tenor": 5.0
    }

    # Mock do repositório
    mocker.patch.object(BeerCRUDRepository, 'create_beer', return_value=MagicMock(**new_beer_data))

    # Testar a criação de uma nova cerveja
    response = client.post("/beer/", data=json.dumps(new_beer_data))

    # Verificar o comportamento esperado
    assert response.status_code == 201
    assert response.json() == new_beer_data


def test_read_beer(mocker):
    # Dados de teste
    beer_data = {
        "id": 1,
        "name": "Test Beer",
        "ibu": 30,
        "style": "Test Style",
        "description": "Test Description",
        "alcohol_tenor": 5.0
    }

    # Mock do repositório
    mocker.patch.object(BeerCRUDRepository, 'read_beers', return_value=[MagicMock(**beer_data)])

    # Testar a leitura de cervejas
    response = client.get("/beer/")

    # Verificar o comportamento esperado
    assert response.status_code == 200
    assert response.json() == [beer_data]


def test_update_beer(mocker):
    # Dados de teste
    beer_id = 1
    updated_beer_data = {
        "name": "Updated Beer",
        "ibu": 40,
        "style": "Updated Style",
        "description": "Updated Description",
        "alcohol_tenor": 6.0
    }

    # Mock do repositório
    mocker.patch.object(BeerCRUDRepository, 'update_beer_by_id', return_value=MagicMock(**updated_beer_data))

    # Testar a atualização de uma cerveja
    response = client.put(f"/beer/{beer_id}", data=json.dumps(updated_beer_data))

    # Verificar o comportamento esperado
    assert response.status_code == 200
    assert response.json() == updated_beer_data


def test_delete_beer(mocker):
    # Dados de teste
    beer_id = 1

    # Mock do repositório
    mocker.patch.object(BeerCRUDRepository, 'delete_beer_by_id', return_value="Beer deleted successfully")

    # Testar a exclusão de uma cerveja
    response = client.delete(f"/beer/{beer_id}")

    # Verificar o comportamento esperado
    assert response.status_code == 200
    assert response.json() == "Beer deleted successfully"
