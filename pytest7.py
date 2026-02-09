def to_upper(s):
    return s.upper()
def get_length(s):
    return len(s)
def test_upper():
    assert to_upper("pytest") == "PYTEST"
def test_length():
    assert get_length("python") == 6