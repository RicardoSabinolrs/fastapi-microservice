from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.infra.settings.manager import settings


def test_create_beer(
        client: TestClient
) -> None:
    data = {
        "name": "Heineken",
        "ibu": 19,
        "style": "Pale Lager",
        "description": "Pure Malt Lager",
        "alcohol_tenor": "5,0%"
    }
    response = client.post(
        f"{settings.API_V1_STR}/beers/", json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["ibu"] == data["ibu"]
    assert content["style"] == data["style"]
    assert content["description"] == data["description"]
    assert content["alcohol_tenor"] == data["alcohol_tenor"]
    assert "id" in content


def test_read_beer(
        client: TestClient, db: Session
) -> None:
    beer = create_random_beer(db)
    response = client.get(
        f"{settings.API_V1_STR}/beers/{beer.id}"
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == beer.name
    assert content["ibu"] == beer.ibu
    assert content["style"] == beer.style
    assert content["description"] == beer.description
    assert content["alcohol_tenor"] == beer.alcohol_tenor
