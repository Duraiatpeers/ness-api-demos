import json

import pytest
from pathlib import Path

def test_create_user_with_api_key(api):

    header = {
        "x-api-key":"reqres-free-v1"
    }

    path = Path("./output/userdata.json")

    with path.open(encoding="utf-8") as fi:
        payload = json.load(fi)

    res = api.post("https://reqres.in/api/users",json=payload, headers=header)
    response_data = res.json()

    print(response_data)
    assert res.status_code == 201

    assert response_data["name"] == "Iniyal"
    assert response_data["job"] == "Test lead"
    assert response_data["id"]
    assert response_data["createdAt"]
    assert "2025" in response_data["createdAt"]
