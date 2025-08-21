import pytest

@pytest.mark.usefixtures("init")
class TestLogin:

    def test_demo1(self):
        assert "abc" not in "welcome"


@pytest.mark.usefixtures("init")
class TestLogin1:

    def test_demo1(self):
        assert "abc" not in "welcome"
