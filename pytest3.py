import pytest
def func(x):
    s = "LOL"
    return s == x
def test_method():
    assert func("LO")

