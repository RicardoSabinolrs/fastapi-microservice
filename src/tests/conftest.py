from typing import Generator

import pytest
from fastapi.testclient import TestClient

from main import beer_app


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(beer_app) as c:
        yield c
