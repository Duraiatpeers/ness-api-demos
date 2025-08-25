import json

import pytest
from pathlib import Path
from jsonschema import validate
from jsonschema import Draft202012Validator
from jsonschema._format import FormatChecker


def test_get_all_users_with_api_key(api):

    header = {
        "x-api-key":"reqres-free-v1"
    }

    path = Path("./output/list_users_schema.json")

    with path.open(encoding="utf-8") as fi:
        dat = json.load(fi)

    user_list_schema = dat


    res = api.get("https://reqres.in/api/users", headers=header)
    response_data = res.json()

    assert res.status_code == 200



    try:
        validator = Draft202012Validator(schema=user_list_schema,format_checker=FormatChecker())
        validate(instance=response_data, schema=user_list_schema)
        print('Schema validation is successful')
    except Exception:
        print("Schema validation failed")
        raise AssertionError("Schema validation failed")

