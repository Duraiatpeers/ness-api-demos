import pytest


def test_create_post_without_bearer_token(api):
    new_post = {
             "id": 233873,
             "user_id": 7440276,
             "title": "Damno vapulus consequatur acies non sint.",
             "body": "Attero thema trepide. Ars causa tempus. Ex compello velit. Asporto thema utroque. Asperiores exercitationem dedico. Vulnus theca varietas. Anser vacuus audeo. Stultus itaque comminor. Antea capto voluptatibus. Eos aut sint. Desparatus beatus vultuosus. Curis carmen voluptas. Voluptatibus defessus ex."
    }

    res = api.post(f"https://gorest.co.in/public/v2/users/7440276/posts", json=new_post)

    # getting response data in json format
    response_data = res.json()
    assert res.status_code == 401


def test_create_post_with_bearer_token(api):
    new_post = {
             "id": 233873,
             "user_id": 7440276,
             "title": "Damno vapulus consequatur acies non sint.",
             "body": "Attero thema trepide. Ars causa tempus. Ex compello velit. Asporto thema utroque. Asperiores exercitationem dedico. Vulnus theca varietas. Anser vacuus audeo. Stultus itaque comminor. Antea capto voluptatibus. Eos aut sint. Desparatus beatus vultuosus. Curis carmen voluptas. Voluptatibus defessus ex."
    }

    header={
        "Authorization": "Bearer da1898aa6c7dfcffafa93e5672cd933dd906921ec29022163e567bc3435c22d1"
    }

    res = api.post(f"https://gorest.co.in/public/v2/users/7440276/posts", json=new_post, headers=header)

    # getting response data in json format
    response_data = res.json()
    assert res.status_code == 201
