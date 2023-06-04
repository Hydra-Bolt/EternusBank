import random

class Account:
    def __init__(self, balance_label, money_label, deposit_label, withdraw_label, transfer_label, ) -> None: 
        self.fullname =fullname
        self.cnic = cnic
        self.account_name = account_name
        self.account_type =account_type
        self.password_create = password_create
        self.account_number = account
        self.balance = 0
    def deposit(self):
        self.balance+=int(self.deposit_label.text())
        return self.balance