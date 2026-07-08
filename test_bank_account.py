import bank_account
import unittest

class TestBankAccount(unittest.TestCase):      

    def test_withdraw(self):
        account = bank_account.BankAccount(100, "caitlin", 1)
        self.assertEqual(account.withdraw(10), 90)
        self.assertEqual(account.withdraw(28.4), 61.6)
        self.assertEqual(account.withdraw(-10), "Withdrawal amount invalid.")

    def test_deposit(self):
        account = bank_account.BankAccount(100, "caitlin", 1)
        self.assertEqual(account.deposit(10), 110)
        self.assertEqual(account.deposit(24.8), 134.8)
        self.assertEqual(account.deposit(-10), "Deposit amount invalid.")
    
    def test_print_current_balance(self):
        account = bank_account.BankAccount(100, "caitlin", 1)
        self.assertEqual(account.print_current_balance(), "Balance is: 100")
