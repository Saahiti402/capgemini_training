import pytest

class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amt):
        self.__balance += amt

    def withdraw(self, amt):
        if amt <= self.__balance:
            self.__balance -= amt

    def get_balance(self):
        return self.__balance


def test_bank_account():
    acc = BankAccount(100)
    acc.deposit(50)
    acc.withdraw(30)
    assert acc.get_balance() == 120
    assert not hasattr(acc, "__balance")