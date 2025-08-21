import pytest

class CustomObj:

    def __init__(self,value):
        self.value = value

    def is_even_number(self):
        return self.value % 2 == 0

@pytest.mark.parametrize("cust_obj_data,expected_even",[(16,True),(4,True),(9,False)])
def test_custom_obj(cust_obj_data,expected_even):
    custom_obj = CustomObj(cust_obj_data)
    assert custom_obj.is_even_number() == expected_even


