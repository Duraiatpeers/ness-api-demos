import pytest


def validate_input(num):
    if not isinstance(num,int):
        raise TypeError("Input should be integer")

def test_validate_input():
    with pytest.raises(TypeError) as err:
        validate_input("abc")

    assert str(err.value) == 'Input should be integer'
