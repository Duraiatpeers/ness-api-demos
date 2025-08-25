import json
from pathlib import Path


def test_de1():
    path = Path("data.json")

    try:
        with path.open(encoding="utf-8") as fil:
            data = json.load(fil)
            print(data)
    except FileNotFoundError:
        print("data.json not found")
    except json.JSONDecodeError as e:
        print(f"Invalid json at line {e.lineno}, col {e.colno}: {e.msg}")




# def test_de1():
#     path = Path("data.json")
#
#     with path.open(encoding="utf-8") as fil:
#         data = json.load(fil)
#
#     print(type(data), data)
#
#     # new_post = '{"id": 233873,"user_id": 7440276,"title": "Damno","body": "Attero thema"}'
#     # data = json.loads(new_post)
#     # print(json.dumps(data,indent=2))
#
#     dat = data.get("sportsperson",[{}])
#     name = dat.get("name","Unknown")
#     sport = dat.get("sports","Unknown")
#     # print(dat)
#     print(name)
#     print(sport)
