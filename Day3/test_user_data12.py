import json

import pytest
from pathlib import Path
from jsonschema import validate

def test_get_all_users_with_api_key(api):

    header = {
        "x-api-key":"reqres-free-v1"
    }

    path = Path("./output/userdt.json")

    with path.open(encoding="utf-8") as fi:
        dat = json.load(fi)

    user_schema = dat


    res = api.get("https://reqres.in/api/users/2", headers=header)
    response_data = res.json()

    assert res.status_code == 200

    validate(instance=response_data,schema=user_schema)

    print('Schema validation is successful')

