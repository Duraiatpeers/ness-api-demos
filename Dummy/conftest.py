import pytest
import requests

@pytest.fixture(scope="session",autouse=True)
def base_url():
    # public demo API
    return "https://reqres.in/api"

@pytest.fixture(scope="session",autouse=True)
def api():
    s = requests.Session()
    s.headers.update({"Accept": "application/json"})
    return s
