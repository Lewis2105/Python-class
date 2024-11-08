class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return f"Amount deposited: {amount}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return f"Amount withdrawn: {amount}"

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def customer_details(self):
        print("Customer Details:")
        print(f"Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")

account = BankAccount("123456789", 1000, "2024-10-15", "John Doe")
print(account.deposit(10000)) 
print(account.withdraw(3000)) 
account.check_balance()  
account.customer_details() 
