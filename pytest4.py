import pytest
def func(x):
    if x %2 == 0:
        return "even"
    else:
        return "odd"
def test_method():
    assert func(int(5)) == "odd"


