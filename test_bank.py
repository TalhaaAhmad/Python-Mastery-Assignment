# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
# Part 12 Challenge - tests for the bank account
import pytest
from part09_oop import BankAccount


@pytest.fixture
def account():
    return BankAccount("Ali", 1000)


def test_deposit(account):
    account.deposit(500)
    assert account.balance == 1500


def test_withdraw(account):
    account.withdraw(300)
    assert account.balance == 700


def test_history(account):
    account.deposit(100)
    account.withdraw(50)
    assert account.history == ["Deposit 100", "Withdraw 50"]


def test_withdraw_too_much(account):
    with pytest.raises(ValueError):
        account.withdraw(5000)


def test_deposit_negative(account):
    with pytest.raises(ValueError):
        account.deposit(-10)
