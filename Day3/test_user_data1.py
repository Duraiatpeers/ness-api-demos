import pytest


def test_get_all_users_with_api_key(api,base_url):

    param = {
        "page":2
    }
    header = {
        "x-api-key":"reqres-free-v1"
    }

    # res = api.get(f"{base_url}/api/users?page=2", headers=header, timeout=10)

    res = api.get(f"{base_url}/api/users",params=param, headers=header, timeout=10)
    response_data = res.json()
    assert response_data["data"][0]["email"] == "michael.lawson@reqres.in"
    assert res.status_code == 200

