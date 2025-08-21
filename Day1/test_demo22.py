import pytest

def test_demo1_string():
    search_result_msg = "you searched for apple iphone15"
    assert search_result_msg == "you searched for apple iphone15"
    assert search_result_msg.split(" ")[4] == 'iphone15'
    assert search_result_msg.split(" ")[3] != 'iphone15'


# @pytest.mark.skip
def test_demo2_list():
    caty_list = ['Books','Toys','Mobile']
    assert "Books" in caty_list
    assert len(caty_list) == 3
    assert caty_list[1] == 'Toys'
    assert sorted(caty_list) == ['Books','Mobile', 'Toys']

def test_demo3_dict():
    browser_details = {
        "browser_name": "chrome",
        "headless": "yes",
        "version": 140.20
    }

    assert browser_details["browser_name"] == 'chrome'
    assert browser_details["version"] == 140.20
    assert "headless" in browser_details
    assert "ostype" in browser_details



