class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"deposit of {amount} successful, new balance: {self.balance}")
        else:
            print("deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("withdrawal denied.")
        elif amount <= 0:
            print("withdrawal amount must be greater than zero.")
        else:
            self.balance -= amount
            print(f"withdrawal of {amount} successful, new balance: {self.balance}")

    def show_balance(self):
        print(f"account owner: {self.owner}, balance: {self.balance}")

name = input("enter owner's name: ")
the_balance = float(input("enter balance: "))

account = Account(name, the_balance)

while True:
    print("options:")
    print("1. deposit")
    print("2. withdraw")
    print("3. show balance")
    print("4. exit")
    choice = input("choose option (1-4): ")
    if choice == "1":
        amount = float(input("enter deposit amount: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("enter withdrawal amount: "))
        account.withdraw(amount)
    elif choice == "3":
        account.show_balance()
    elif choice == "4":
        print("exiting...")
        break
    else:
        print("invalid choice, choose between 1-4.")