import pytest

class CustomObj:

    def __init__(self,value):
        self.value = value

    def get_double_the_value(self):
        return self.value * 2


def test_custom_obj():
    custom_obj = CustomObj(10)
    assert custom_obj.get_double_the_value() == 20


