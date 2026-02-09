class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    pass


class Developer(Employee):
    pass


def test_inheritance():
    m = Manager("Alice", 80000)
    d = Developer("Bob", 60000)

    assert m.name == "Alice"
    assert d.salary == 60000