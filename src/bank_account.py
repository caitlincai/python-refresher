class BankAccount:
    def __init__(self, balance, name, accountNumber):
        self.balance = balance
        self.name = name
        self.accountNumber = accountNumber
        
    def withdraw(self, amount: int | float):
        if amount > 0:
            self.balance -= amount
            return self.balance
        elif amount <= 0 or self.balance-amount < 0:
            return "Withdrawal amount invalid."

    def deposit(self, amount: int | float):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            return "Deposit amount invalid."
    
    def print_current_balance(self) -> str:
        return f"Balance is: {self.balance}"