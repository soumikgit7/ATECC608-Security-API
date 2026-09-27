
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def generate_key():
    response = client.post("/api/v1/keys/generate")

    assert response.status_code == 200

    return response.json()["key_id"]


def test_ecdh_shared_secret_matches():
    # Generate Alice's key pair
    alice_key_id = generate_key()

    # Generate Bob's key pair
    bob_key_id = generate_key()

    # Alice derives secret using:
    # Alice private key + Bob public key
    alice_response = client.post(
        "/api/v1/ecdh/derive",
        json={
            "private_key_id": alice_key_id,
            "peer_key_id": bob_key_id
        }
    )

    assert alice_response.status_code == 200

    alice_result = alice_response.json()

    assert alice_result["algorithm"] == "ECDH"
    assert alice_result["curve"] == "secp256r1"
    assert "shared_secret" in alice_result

    # Bob derives secret using:
    # Bob private key + Alice public key
    bob_response = client.post(
        "/api/v1/ecdh/derive",
        json={
            "private_key_id": bob_key_id,
            "peer_key_id": alice_key_id
        }
    )

    assert bob_response.status_code == 200

    bob_result = bob_response.json()

    assert bob_result["algorithm"] == "ECDH"
    assert bob_result["curve"] == "secp256r1"
    assert "shared_secret" in bob_result

    # The two parties must derive the same shared secret
    assert alice_result["shared_secret"] == bob_result["shared_secret"]


def test_ecdh_missing_private_key():
    bob_key_id = generate_key()

    response = client.post(
        "/api/v1/ecdh/derive",
        json={
            "private_key_id": "non-existent-key",
            "peer_key_id": bob_key_id
        }
    )

    assert response.status_code == 404


def test_ecdh_missing_peer_key():
    alice_key_id = generate_key()

    response = client.post(
        "/api/v1/ecdh/derive",
        json={
            "private_key_id": alice_key_id,
            "peer_key_id": "non-existent-key"
        }
    )

    assert response.status_code == 404
