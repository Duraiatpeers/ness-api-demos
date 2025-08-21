import pytest


def div_by_zero(num1,num2):
    return num1/num2

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError) as err:
        div_by_zero(10,0)

    assert str(err.value) == 'division by zero'
