import pytest


def add(num1,num2):
    return num1+num2

def test_two():
    result = add(20,30)
    assert result == 50


