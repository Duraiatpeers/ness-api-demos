import json

import pytest
from pathlib import Path

def test_get_all_users_with_api_key(api):

    header = {
        "x-api-key":"reqres-free-v1"
    }

    res = api.get("https://reqres.in/api/users/2", headers=header)
    response_data = res.json()

    assert res.status_code == 200

    path = Path("./output/users.json")

    with path.open("w", encoding="utf-8") as fi:
        json.dump(response_data,fi, indent=2)

