import json
import os

FILE_NAME = "data.json"

class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance
        }


# ---------------- File Handling ---------------- #

def load_accounts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return data
    return []

def save_accounts(accounts):
    with open(FILE_NAME, "w") as file:
        json.dump(accounts, file, indent=4)


# ---------------- Menu Functions ---------------- #

def create_account(accounts):
    try:
        acc_no = input("Enter Account Number: ")
        name = input("Enter Name: ")
        balance = float(input("Enter Initial Balance: "))

        account = BankAccount(acc_no, name, balance)
        accounts.append(account.to_dict())
        save_accounts(accounts)

        print("Account created successfully!\n")

    except ValueError as e:
        print("Error:", e)

def deposit_money(accounts):
    try:
        acc_no = input("Enter Account Number: ")
        amount = float(input("Enter Amount to Deposit: "))

        for acc in accounts:
            if acc["account_number"] == acc_no:
                account = BankAccount(acc["account_number"], acc["name"], acc["balance"])
                account.deposit(amount)
                acc["balance"] = account.balance
                save_accounts(accounts)
                print("Deposit successful!\n")
                return

        print("Account not found.\n")

    except ValueError as e:
        print("Error:", e)

def withdraw_money(accounts):
    try:
        acc_no = input("Enter Account Number: ")
        amount = float(input("Enter Amount to Withdraw: "))

        for acc in accounts:
            if acc["account_number"] == acc_no:
                account = BankAccount(acc["account_number"], acc["name"], acc["balance"])
                account.withdraw(amount)
                acc["balance"] = account.balance
                save_accounts(accounts)
                print("Withdrawal successful!\n")
                return

        print("Account not found.\n")

    except ValueError as e:
        print("Error:", e)

def check_balance(accounts):
    acc_no = input("Enter Account Number: ")
    for acc in accounts:
        if acc["account_number"] == acc_no:
            print(f"Account Holder: {acc['name']}")
            print(f"Balance: ₹{acc['balance']}\n")
            return
    print("Account not found.\n")


# ---------------- Main Menu ---------------- #

def main():
    accounts = load_accounts()

    while True:
        print("===== Smart Bank CLI =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit_money(accounts)
        elif choice == "3":
            withdraw_money(accounts)
        elif choice == "4":
            check_balance(accounts)
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice!\n")


if __name__ == "__main__":
    main()