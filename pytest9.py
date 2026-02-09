import pytest
def div(a, b):
    return a/b
def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        div(5, 0)