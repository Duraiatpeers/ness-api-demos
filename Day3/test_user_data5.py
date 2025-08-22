import pytest


def test_user_auth_test(api,base_url):

    response = api.get(
        "https://httpbin.org/basic-auth/user/passwd",
        auth=("user", "passwd")
    )

    res_data = response.json()

    assert res_data["authenticated"]
    assert res_data["user"]
    assert res_data["authenticated"] == True
    assert res_data["user"] == 'user'

