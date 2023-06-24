class Account:
    def __init__(self, account_info) -> None:
        self.account_info = account_info
        self.balance = self.account_info["Balance"]

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        return self.balance
    def balanceInquiry(self):
        return self.balance


class SavingsAccount(Account):
    pass


class CheckingAccount(Account):
    def __init__(self, account_info) -> None:
        super().__init__(account_info)
        self.overdraft = self.account_info["Overdraft"]

    def withdraw(self, amount):
        if self.balance+self.overdraft > amount:
            self.balance -= amount
        return self.balance


class Loan(Account):
    def __init__(self, account_info) -> None:
        self.account_info = account_info
        self.loan = self.account_info["Loan"]
        self.interest = self.account_info["Added"]
        self.balance = self.account_info["Net Pay"]

    def deposit(self, amount):
        return super().deposit(amount)