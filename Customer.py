from Account import CheckingAccount, SavingsAccount, Loan
from datetime import date



class Customer:
    def __init__(self, current_account=None, balance_labels=None, overdraft_label=None, deposit_edit=None, withdraw_edit=None) -> None:
        self.current_account = current_account
        self.balance_labels = balance_labels
        self.overdraft_label = overdraft_label
        self.deposit_edit = deposit_edit
        self.withdraw_edit = withdraw_edit
        self.interest_label = overdraft_label
        if self.current_account["Account Type"] == "Loan Account":
            self.current = Loan(self.current_account)

        elif self.current_account["Account Type"] == "Checking Account":
            self.current = CheckingAccount(self.current_account)
        else:
            self.current = SavingsAccount(self.current_account)

    def deposit(self):
        current_date = date.today()
        formatted_date = current_date.strftime("%d/%m/%Y")
        try:
            amount = float(self.deposit_edit.text())
            self.deposit_edit.setText("")
        except:
            return
        self.current_account["Balance"] = self.current.deposit(amount)
        self.current_account["Transactions"].append(["Deposit", formatted_date, amount])
        self.balanceUpdate()
        

    def withdraw(self):
                
        current_date = date.today()
        formatted_date = current_date.strftime("%d/%m/%Y")
        try:
            amount = float(self.withdraw_edit.text())

            self.withdraw_edit.setText("")
        except:

            return

        if self.current_account["Account Type"] == "Loan Account":
            for label in self.balance_labels:
                net = (float(label.text().strip("$"))-amount)
                label.setText(f"${max(net, 0)}")
            self.current_account["Net Pay"] = self.current.withdraw(amount)

            return amount
        init = self.current_account["Balance"]
        self.current_account["Balance"] = self.current.withdraw(amount)
        fin = self.current_account["Balance"]
        if init!=fin:
            self.current_account["Transactions"].append(["Withdraw", formatted_date, amount])
        self.balanceUpdate()

    def balanceUpdate(self):

        for label in self.balance_labels:
            label.setText(f"${self.current_account['Balance']}")
        if self.current_account["Account Type"] == "Savings Account":
            self.interest_label.setText(f"+${round(self.current_account['Balance']*self.current_account['Interest Rate'])}/Daily")
            