
import pytest

@pytest.fixture(scope='session')
def init():
    print('Setup - pre method')
    pass
    print('Tear down')

