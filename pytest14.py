import unittest
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
class TestStudent(unittest.TestCase):
    def test_constructor(self):
        s = Student("Riya", 101)
        self.assertEqual(s.name, "Riya")
        self.assertEqual(s.roll_no, 101)
if __name__ == "__main__":
    unittest.main()