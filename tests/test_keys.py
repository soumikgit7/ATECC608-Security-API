from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
def test_generate_key():
    response = client.post("/api/v1/keys/generate")
    assert response.status_code == 200
    data = response.json()
    assert "key_id" in data
    assert len(data["key_id"]) > 0
def test_generate_multiple_keys():
    response1 = client.post("/api/v1/keys/generate")
    response2 = client.post("/api/v1/keys/generate")

    assert response1.status_code == 200
    assert response2.status_code == 200

    key1 = response1.json()["key_id"]
    key2 = response2.json()["key_id"]

    # Every generated key should have a unique ID
    assert key1 != key2


def test_generated_key_has_public_key():
    response = client.post("/api/v1/keys/generate")

    assert response.status_code == 200

    data = response.json()

    assert "key_id" in data
    assert "public_key" in data
    assert len(data["public_key"]) > 0
