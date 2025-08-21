import pytest

@pytest.fixture
def init():
    print('Setup - pre method')
    pass
    print('Tear down')

def test_demo1(init):
    print('Inside demo1')
    assert True


def test_demo2(init):
    print('Inside demo2')
    assert True
