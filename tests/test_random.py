
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_generate_random_bytes():
    response = client.post(
        "/api/v1/random/generate?length=32"
    )

    assert response.status_code == 200

    result = response.json()

    assert "length" in result
    assert "random_data" in result

    assert result["length"] == 32
    assert len(result["random_data"]) == 64


def test_random_length():
    response = client.post(
        "/api/v1/random/generate?length=16"
    )

    assert response.status_code == 200

    result = response.json()

    assert result["length"] == 16

    # 16 bytes represented as hexadecimal = 32 characters
    assert len(result["random_data"]) == 32


def test_random_values_are_different():
    response1 = client.post(
        "/api/v1/random/generate?length=32"
    )

    response2 = client.post(
        "/api/v1/random/generate?length=32"
    )

    assert response1.status_code == 200
    assert response2.status_code == 200

    random1 = response1.json()["random_data"]
    random2 = response2.json()["random_data"]

    assert random1 != random2


def test_random_length_zero():
    response = client.post(
        "/api/v1/random/generate?length=0"
    )

    assert response.status_code == 400


def test_random_length_too_large():
    response = client.post(
        "/api/v1/random/generate?length=1025"
    )

    assert response.status_code == 400
