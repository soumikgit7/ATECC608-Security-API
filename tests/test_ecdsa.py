
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_ecdsa_sign():
    # Generate a key
    key_response = client.post("/api/v1/keys/generate")

    assert key_response.status_code == 200

    key_data = key_response.json()
    key_id = key_data["key_id"]

    # Sign data
    response = client.post(
        "/api/v1/ecdsa/sign",
        json={
            "key_id": key_id,
            "data": "hello"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["algorithm"] == "ECDSA"
    assert data["key_id"] == key_id
    assert "signature" in data
    assert len(data["signature"]) > 0


def test_ecdsa_verify_valid_signature():
    # Generate a key
    key_response = client.post("/api/v1/keys/generate")

    assert key_response.status_code == 200

    key_id = key_response.json()["key_id"]

    # Sign data
    sign_response = client.post(
        "/api/v1/ecdsa/sign",
        json={
            "key_id": key_id,
            "data": "hello"
        }
    )

    assert sign_response.status_code == 200

    signature = sign_response.json()["signature"]

    # Verify signature
    verify_response = client.post(
        "/api/v1/ecdsa/verify",
        json={
            "key_id": key_id,
            "data": "hello",
            "signature": signature
        }
    )

    assert verify_response.status_code == 200

    result = verify_response.json()

    assert result["algorithm"] == "ECDSA"
    assert result["key_id"] == key_id
    assert result["valid"] is True


def test_ecdsa_verify_invalid_signature():
    # Generate a key
    key_response = client.post("/api/v1/keys/generate")

    assert key_response.status_code == 200

    key_id = key_response.json()["key_id"]

    # Sign original data
    sign_response = client.post(
        "/api/v1/ecdsa/sign",
        json={
            "key_id": key_id,
            "data": "hello"
        }
    )

    assert sign_response.status_code == 200

    signature = sign_response.json()["signature"]

    # Verify against modified data
    verify_response = client.post(
        "/api/v1/ecdsa/verify",
        json={
            "key_id": key_id,
            "data": "hello2",
            "signature": signature
        }
    )

    assert verify_response.status_code == 200

    result = verify_response.json()

    assert result["valid"] is False
