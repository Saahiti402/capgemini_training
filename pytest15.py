import unittest

# =========================
#   Class Definitions
# =========================

class Bank:
    def getInterestRate(self):
        return 0.0


class SBI(Bank):
    def getInterestRate(self):
        return 5.5


class HDFC(Bank):
    def getInterestRate(self):
        return 6.2


class ICICI(Bank):
    def getInterestRate(self):
        return 6.0
class TestBankInterestRates(unittest.TestCase):

    def test_base_bank(self):
        self.assertEqual(Bank().getInterestRate(), 0.0)

    def test_sbi(self):
        self.assertEqual(SBI().getInterestRate(), 5.5)

    def test_hdfc(self):
        self.assertEqual(HDFC().getInterestRate(), 6.2)

if __name__ == "__main__":
    unittest.main()
