from Bank import Bank
class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds. Current balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
    
    def get_balance(self):
        print(f"Current balance: {self.balance}")
    
    def transfer(self, to_account, amount):
        if amount > self.balance:
            print(f"Insufficient funds. Current balance: {self.balance}")
        else:
            self.balance -= amount
            to_account.balance += amount
            print(f"Transfer of {amount} successful. Your new balance: {self.balance}. Receiver's new balance: {to_account.balance}")

# Example usage:
account1 = BankAccount("John Doe", "123456789", 1000)
account2 = BankAccount("Jane Smith", "987654321", 500)

# Deposit to account1
account1.deposit(200)

# Withdraw from account2
account2.withdraw(100)

# Get balances
account1.get_balance()
account2.get_balance()

# Transfer from account1 to account2
account1.transfer(account2, 300)

# Get balances after transfer
account1.get_balance()
account2.get_balance()