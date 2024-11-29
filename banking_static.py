class Banking:
    def __init__(self, user_name, initial_balance):
        self.user_name = user_name
        self.initial_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.initial_balance += amount
            return f"Deposit successful. {amount} Taka Added"
        else:
            return "Invalid deposit amount. Deposit failed."

    def check_balance(self):
        return f"Balances: {self.initial_balance} Taka only"

    def withdraw(self, amount):
        if amount <= 0:  # Guard condition
            return "Invalid withdrawal amount. Withdrawal failed."

        if amount > self.initial_balance:  # Check for insufficient balance
            return "Insufficient balance. Withdrawal failed."

        self.initial_balance -= amount  # Perform withdrawal
        return f"Withdrawal Amount: {amount}, Withdrawal successful. Remaining balance: {self.initial_balance} Taka."


account = Banking("Rahim", 1000)

print(
    f"Name: {account.user_name}, initial balance: {account.initial_balance} Taka only "
)
print(f"{account.user_name}, {account.deposit(1500)}")
print(f"{account.user_name}, {account.check_balance()}")
print(f"{account.user_name}, {account.withdraw(100)}")
