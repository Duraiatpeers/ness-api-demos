import pytest


def test_get_user(api, base_url):
    resp = api.get(f"{base_url}/users/2", timeout=10)
    assert resp.status_code == 200
    assert resp.headers.get("Content-Type", "").startswith("application/json")

    data = resp.json()
    assert "data" in data
    assert data["data"]["id"] == 2
    assert data["data"]["email"].endswith("@reqres.in")

def test_create_user(api, base_url):
    payload = {"name": "morpheus", "job": "leader"}
    header = {
        "x-api-key": "reqres-free-v1"
    }
    resp = api.post(f"https://reqres.in/api/users", json=payload, timeout=10, headers=header)
    assert resp.status_code == 201
    assert resp.headers.get("Content-Type", "").startswith("application/json")

    data = resp.json()
    # Echoed back by the API
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    # Created resource metadata
    assert "id" in data and data["id"]
    assert "createdAt" in data
