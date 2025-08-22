import pytest


def test_delete_user_with_api_key(api,base_url):


    # header to include the access key
    header = {
        "x-api-key":"reqres-free-v1"
    }

    user_id = 2
    res = api.delete(f"{base_url}/api/users/{user_id}",headers=header, timeout=10)
    response_data = res.text

    assert res.status_code == 204
    assert response_data == ""
