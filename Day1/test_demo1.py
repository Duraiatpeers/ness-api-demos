import pytest


def add(num1,num2):
    return num1+num2

def test_one():
    result = add(20,30)
    assert result == 50



browsers = ['chrome','edge', 'firefox']

def test_data_check():
    assert 'chrome' in browsers

