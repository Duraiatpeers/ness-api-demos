import pytest


def test_update_user_with_api_key(api,base_url):

    existing_user={
        "name":"morpheus",
        "job":"VP"
    }

    # header to include the access key
    header = {
        "x-api-key":"reqres-free-v1"
    }

    user_id = 2
    res = api.put(f"{base_url}/api/users/{user_id}",json=existing_user, headers=header, timeout=10)
    response_data = res.json()

    print(response_data)
    assert res.status_code == 200

    assert response_data["name"] == "morpheus"
    assert response_data["job"] == "VP"
    # assert response_data["createdAt"]
    assert response_data["updatedAt"]

    assert "2025" in response_data["updatedAt"]
