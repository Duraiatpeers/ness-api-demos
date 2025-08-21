import pytest

def d1(n):
    if n ==0:
        raise ZeroDivisionError("Number is zero")
    return n/0

def test_d1():
    with pytest.raises(ZeroDivisionError) as e:
        d1(0)
    assert "zero" in str(e.value)
