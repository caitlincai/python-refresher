import bank_account
import unittest

class TestBankAccount(unittest.TestCase):      

    def test_withdraw(self):
        account = bank_account.BankAccount(100, "caitlin", 1)
        self.assertEqual(account.withdraw(10), 90)
        self.assertEqual(account.withdraw(20), 70)
        self.assertEqual(account.withdraw(-10), 80)

    def test_deposit(self):
        account = bank_account.BankAccount(100, "caitlin", 1)
        self.assertEqual(account.deposit(10), 110)
        self.assertEqual(account.deposit(20), 130)
        self.assertEqual(account.deposit(-10), 120)
    
    def test_print_current_balance(self):
        account = bank_account.BankAccount(100, "caitlin", 1)
        self.assertEqual(account.print_current_balance(), "Balance is: 100")
