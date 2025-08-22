# https://reqres.in/api/users?page=2
import pytest
import requests


@pytest.fixture(scope="session", autouse=True)
def base_url():
    return "https://reqres.in"


@pytest.fixture(scope="session", autouse=True)
def api():
    sess = requests.session()
    sess.headers.update({"Accept": "application/json"})
    return sess
