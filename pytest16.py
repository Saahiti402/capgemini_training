import unittest
class Bank:
    def getInterestRate(self) -> float:
        return 0.0


class SBI(Bank):
    def getInterestRate(self) -> float:  
        return 5.5

class TestSingleInheritance(unittest.TestCase):

    def test_base_class(self):
        bank = Bank()
        self.assertEqual(bank.getInterestRate(), 0.0)

    def test_child_class(self):
        sbi = SBI()
        self.assertEqual(sbi.getInterestRate(), 5.5)

    def test_inheritance(self):
        sbi: Bank = SBI()
        self.assertIsInstance(sbi, Bank)
        self.assertEqual(sbi.getInterestRate(), 5.5)


if __name__ == "__main__":
    unittest.main()
