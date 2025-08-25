# pip install requests jsonschema

import pytest
import json
import requests
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

def load_schema(path: str | Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def assert_valid_schema(instance: dict, schema: dict) -> None:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(instance), key=lambda e: (list(e.path), e.message))
    if errors:
        msg = "\n".join(f"- at {list(e.path)}: {e.message}" for e in errors)
        raise AssertionError(f"Schema validation failed:\n{msg}")

def get_json(url: str, **kwargs) -> dict:
    r = requests.get(url, timeout=15, headers={"Accept": "application/json"}, **kwargs)
    r.raise_for_status()
    return r.json()

def test1():
    schema = load_schema("user_schema.json")  # or keep it inline
    data = get_json("https://reqres.in/api/users/2")
    assert_valid_schema(data, schema)
    print("✅ Single-object response matches schema")

    # EXAMPLE B: list/paginated response
    list_schema = load_schema("list_users_schema.json")
    data2 = get_json("https://reqres.in/api/users", params={"page": 2})
    assert_valid_schema(data2, list_schema)
    print("✅ List response matches schema")
