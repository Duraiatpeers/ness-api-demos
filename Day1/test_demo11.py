import pytest

@pytest.mark.smoke
def test_demo1():
    assert True

@pytest.mark.regression
def test_demo2():
    assert False

# @pytest.mark.smoke
@pytest.mark.basic
def test_demo3():
    msg = "Welcome to Pytest scripting"
    assert "Pytest" in msg.split(" ")



