import requests


base_url = 'https://reqres.in'
# /api/users/2

def test_get_user():

    req = requests.session()
    req.headers.update({"Accept":"application/json"})

    response = req.get(f"{base_url}/api/users/2", timeout=10)

    assert response.status_code == 200

    response_data = response.json()

    assert "email" in response_data["data"]
    assert response_data["data"]["last_name"] == "Weaver"
    assert "contentcaddy.io" in response_data["support"]["url"]


