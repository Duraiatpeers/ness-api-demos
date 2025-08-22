import pytest


def test_get_all_users_without_api_key(api,base_url):
    res = api.get(f"{base_url}/api/users?page=2",timeout=10)
    # print(res)

    # print(res.text)
    # print(res.json())
    response_data = res.json()

    # print(response_data["data"])
    # print(response_data["data"][0]["email"])
    assert response_data["data"][0]["email"] == "michael.lawson@reqres.in"

    # print(res.headers)
    # print(res.headers["Content-Type"])
    assert res.status_code == 401

    # print(type(res.content))
    # print(type(res.text))
    # print("total" in res.text)

    print(res.request.url)

