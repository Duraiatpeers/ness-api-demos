import requests
from requests.exceptions import HTTPError


def test_put_update_user(api, base_url):
    payload = {"name": "Ada", "job": "Engineer"}
    header = {
        "x-api-key": "reqres-free-v1"
    }
    resp = api.put(f"{base_url}/users/2", json=payload, timeout=10,headers=header)

    # Status + content-type
    assert resp.status_code == 200
    ctype = resp.headers.get("content-type", "")
    assert ctype.lower().startswith("application/json")

    # Body echoes fields and includes metadata
    data = resp.json()
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    assert "updatedAt" in data and data["updatedAt"]  # server timestamp present

def test_delete_user(api, base_url):
    header = {
        "x-api-key": "reqres-free-v1"
    }
    resp = api.delete(f"{base_url}/users/2", timeout=10, headers=header)

    # Expect 204 No Content and empty body
    assert resp.status_code == 204
    assert resp.text == ""  # DELETE returns no content on this API


def test_get_user_by_id__path_variable(api, base_url):
    # Path variable: /users/{id}
    user_id = 2
    header = {
        "x-api-key": "reqres-free-v1"
    }

    resp = api.get(f"{base_url}/users/{user_id}", timeout=10, headers=header)

    assert resp.status_code == 200
    assert resp.headers.get("content-type", "").lower().startswith("application/json")

    body = resp.json()
    assert "data" in body
    assert body["data"]["id"] == user_id
    assert body["data"]["email"].endswith("@reqres.in")


def test_get_users__query_params(api, base_url):
    # Query params: /users?page=2
    params = {"page": 2}

    header = {
        "x-api-key": "reqres-free-v1"
    }

    resp = api.get(f"{base_url}/users", params=params, timeout=10,headers=header)

    assert resp.status_code == 200
    assert resp.headers.get("content-type", "").lower().startswith("application/json")

    body = resp.json()
    assert body["page"] == 2
    assert isinstance(body.get("data"), list) and len(body["data"]) > 0
    for user in body["data"]:
        assert "id" in user and "email" in user


def test_get_user_by_id_with_query_param__combined(api, base_url):
    # (Optional) Path + query together: /users/2?delay=1
    params = {"delay": 1}

    header = {
        "x-api-key": "reqres-free-v1"
    }

    resp = api.get(f"{base_url}/users/2", params=params, timeout=10,headers=header)

    assert resp.ok
    assert resp.headers.get("content-type", "").lower().startswith("application/json")


def test_a():
    response = requests.get(
        "https://api.github.com/search/repositories",
        params={"q": "language:python", "sort": "stars", "order": "desc"},
    )

    json_response = response.json()
    popular_repositories = json_response["items"]
    for repo in popular_repositories[:3]:
        print(f"Name: {repo['name']}")
        print(f"Description: {repo['description']}")
        print(f"Stars: {repo['stargazers_count']}\n")


