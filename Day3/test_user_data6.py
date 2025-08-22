import pytest
import requests
from requests.exceptions import HTTPError

@pytest.mark.parametrize("url",[("https://api.github.com"),("https://api.github.com/invalid")])
def test_http_error(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as httperror:
        print('Http Error')
        assert response.status_code == 404
    except Exception as err:
        print(err)
    else:
        assert response.status_code == 200
        print('Success')





# def test_http_error():
#     urls = ["https://api.github.com", "https://api.github.com/invalid"]
#
#     for url in urls:
#
#         try:
#             response = requests.get(url)
#             response.raise_for_status()
#         except HTTPError as httperror:
#                 print('Http Error')
#         except Exception as err:
#             print(err)
#         else:
#             print('Success')

