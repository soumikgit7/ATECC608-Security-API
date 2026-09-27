
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_sha256_hash():
    response = client.post(
        "/api/v1/hash/sha256",
        json={
            "data": "hello"
        }
    )

    assert response.status_code == 200

    result = response.json()

    assert result["algorithm"] == "SHA-256"
    assert "hash" in result
    assert len(result["hash"]) == 64


def test_sha256_same_input_same_hash():
    response1 = client.post(
        "/api/v1/hash/sha256",
        json={
            "data": "hello"
        }
    )

    response2 = client.post(
        "/api/v1/hash/sha256",
        json={
            "data": "hello"
        }
    )

    assert response1.status_code == 200
    assert response2.status_code == 200

    hash1 = response1.json()["hash"]
    hash2 = response2.json()["hash"]

    assert hash1 == hash2


def test_sha256_different_input_different_hash():
    response1 = client.post(
        "/api/v1/hash/sha256",
        json={
            "data": "hello"
        }
    )

    response2 = client.post(
        "/api/v1/hash/sha256",
        json={
            "data": "hello2"
        }
    )

    assert response1.status_code == 200
    assert response2.status_code == 200

    hash1 = response1.json()["hash"]
    hash2 = response2.json()["hash"]

    assert hash1 != hash2
