import json

import pytest
from pathlib import Path
from jsonschema import validate

def test_get_all_users_with_api_key(api):

    header = {
        "x-api-key":"reqres-free-v1"
    }

    user_schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "required": ["data"],
            "properties": {
                "data": {
                    "type": "object",
                    "required": ["id", "email", "first_name", "last_name"],
                    "properties": {
                        "id": {"type": "integer"},
                        "email": {"type": "string", "format": "email"},
                        "first_name": {"type": "string"},
                        "last_name": {"type": "string"},
                        "avatar": {"type": "string", "format": "uri"}
                    },
                    "additionalProperties": True
                },
                "support": {"type": "object"}
            },
            "additionalProperties": True
        }



    res = api.get("https://reqres.in/api/users/2", headers=header)
    response_data = res.json()

    assert res.status_code == 200

    validate(instance=response_data,schema=user_schema)

    print('Schema validation is successful')

