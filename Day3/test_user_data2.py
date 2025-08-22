import pytest


def test_create_user_without_api_key(api,base_url):

    # payload
    new_user = {
        "name": "Iniyal",
        "job": "Test lead"
    }

    #post request
    res = api.post(f"{base_url}/api/users", json=new_user, timeout=10)

    # getting response data in json format
    response_data = res.json()

    assert res.status_code == 401

def test_create_user_with_api_key(api,base_url):

    new_user={
        "name": "Iniyal",
        "job": "Test lead"
    }

    # header to include the access key
    header = {
        "x-api-key":"reqres-free-v1"
    }

    res = api.post(f"{base_url}/api/users",json=new_user, headers=header, timeout=10)
    response_data = res.json()

    print(response_data)
    assert res.status_code == 201

    assert response_data["name"] == "Iniyal"
    assert response_data["job"] == "Test lead"
    assert response_data["id"]
    assert response_data["createdAt"]
    assert "2025" in response_data["createdAt"]
