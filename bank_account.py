class BankAccount:
    def __init__(self, balance, name, accountNumber):
        self.balance = balance
        self.name = name
        self.accountNumber = accountNumber
        
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def print_current_balance(self):
        return f"Balance is: {self.balance}"
    
# def __main__():
#     self.print_current_balance()

# if __name__ == "__main__":
#     __main__()