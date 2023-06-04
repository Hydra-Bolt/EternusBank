
import DesignClass
import time
import sys
import random
from datetime import datetime, timedelta
import importlib
from PyQt5 import QtCore, QtGui, QtWidgets
importlib.reload(DesignClass)

class Bank(DesignClass.MasterGUI):
    
    def __init__(self, MainWindow: QtWidgets.QMainWindow) -> None:
        super().__init__()
        self.setupDB()
        self.MainWindow = MainWindow
        self.setupUi_intro(self.MainWindow)
        self.MainWindow.setWindowIcon(QtGui.QIcon('logo.png'))
        self.MainWindow.show()

    def generate_credit_card_number(self):
        # Generate the first 6 digits (Issuer Identification Number)
        iin = random.choice(['4', '5', '37', '6']) + ''.join(random.choice('0123456789') for _ in range(5))

        # Generate the remaining digits (Account Number)
        account_number = ''.join(random.choice('0123456789') for _ in range(9))

        # Combine the IIN and account number
        card_number = iin + account_number
        return card_number
    def generate_expiry_date(self):
        # Set the current date
        current_date = datetime.now()

        # Calculate the maximum expiry duration (e.g., 5 years from the current date)
        max_expiry_duration = timedelta(days=365 * 5)

        # Calculate the maximum expiry date
        max_expiry_date = current_date + max_expiry_duration

        return [max_expiry_date.strftime("%m/%Y"), max_expiry_date.strftime("%B"), max_expiry_date.strftime("%Y")]
    def createAccount(self):
        # sourcery skip: simplify-dictionary-update, simplify-empty-collection-comparison, swap-if-else-branches, use-named-expression
        # List of data fields to be filled
        filling_data = ["Full Name", "CNIC"]

        # List of data entered by the user
        list_of_data = [self.fullname.text(), self.cnic.text()]

        # Generate a random account number
        account_number = "ETR-" + "".join([str(random.randint(0, 9)) for _ in range(6)]) + "-" + "".join(
            [str(random.randint(0, 9)) for _ in range(6)])

        print(account_number)

        # List of account information fields
        accounts = ["Account Name", "Account Number", "Account Type", "Password"]

        # List of account data entered by the user
        accounts_data = [self.account_name.text(), account_number, self.accountype.currentText(), self.password_create.text()]

        # Create a dictionary with the filling data and corresponding user-entered data
        self.output = {filling_data[i]: list_of_data[i] for i in range(len(list_of_data))}

        # Check if any of the required information fields are empty
        infolist = [i == "" for i in list_of_data]
        accountlist = [i == "" for i in accounts_data]

        # Display an error message if any required field is empty
        if any(infolist) or any(accountlist):
            try:
                print(f"{filling_data[infolist.index(True)]} isn't filled")
            except Exception:
                print(f"{accounts[accountlist.index(True)]} isn't filled")
        else:
            # Create dictionaries for user information and account information

            info = {filling_data[i]: list_of_data[i] for i in range(len(list_of_data))}
            self.account = {accounts[i]: accounts_data[i] for i in range(len(accounts_data))}
            if self.account["Account Type"] != "Loan Account":
                self.account["Balance"] = 0
                self.account["Card Number"] = self.generate_credit_card_number()
                self.account["Expiry Date"] = self.generate_expiry_date()
                self.account["Transactions"] = []
                if self.account["Account Type"] == "Checking Account":
                    self.account["Overdraft"] = 500
                else:
                    print("savings")
                    self.account["Interest Rate"] = 0.0000022831
            else:
                self.MainWindow.close()
                self.loan_application = QtWidgets.QDialog()
                self.setupLoanApp(self.loan_application)
                self.loan_application.show()
                print("ran")
            # Check if the user already exists in the database

            result = list(self.userAccountInfo.find({"CNIC": info["CNIC"]}))
            if result != []:
                print("found")
                update = {"$push": {"Accounts": self.account}}
                self.userAccountInfo.update_one({"CNIC": info["CNIC"]}, update=update)
            else:
                print('here')
                info |= {"Accounts": [self.account]}
                self.userAccountInfo.insert_one(info)
            if self.account["Account Type"] == "Loan Account":
                return
            self.openHomeWindow()
    
    def checkCredentials(self):
        filling_data = ["CNIC", "Account Name", "Password"]
        list_of_data = [self.cnic_line_edit.text(),self.account_edit_login.text(),self.password_login_edit.text()]
        infolist = [i == "" for i in list_of_data]
        if any(infolist):
            print(f"{filling_data[infolist.index(True)]} isnt filled")
        else:
            info = {filling_data[i]: list_of_data[i] for i in range(len(list_of_data))}
            self.output = self.userAccountInfo.find_one({"CNIC":info["CNIC"]})

            print(self.output)
            if self.output is None:
                print("dont have an account")
            else:
                accounts = self.output["Accounts"]
                for account in accounts:
                    if account["Account Name"] == info["Account Name"]:
                        break
                else:
                       
                    print("Incorrect Account Name")
                if account["Password"] != info["Password"]:
                    print("Incorrect Password")
                elif account["Account Type"] == "Loan Account":
                    self.account = account
                    self.openLoanWindow()
                else:
                    self.account = account
                    self.openHomeWindow()
        
    def openHomeWindow(self):
        super().openHomeWindow()
        self.name_top.setText(f'Welcome, {self.output["Full Name"]}')
        self.name_card.setText(f'{self.output["Full Name"]}')
        self.name_2.setText(f'{self.output["Full Name"]}')
        self.expiry_date.setText(self.account['Expiry Date'][0])
        self.expiry.setText(self.account['Expiry Date'][0])
        self.month.setText(self.account['Expiry Date'][1])
        self.year.setText(self.account['Expiry Date'][2])
        self.number_2.setText(self.account["Card Number"])
        self.acc_number.setText(self.account["Card Number"])
        self.number.setText(self.account["Card Number"])
        self.balance_amount.setText(f"${self.account['Balance']}")
        self.money_label.setText(f"${self.account['Balance']}")
        if self.account["Account Type"] == "Checking Account":
            
            self.overdraft.setText(f"+${self.account['Overdraft']}")
            self.checkingAccount()
        else:
            
            self.overdraft.setText(f"{self.account['Interest Rate']*self.account['Balance']}")
            self.savingsAccount()
    def setupDB(self):
                
        from pymongo.mongo_client import MongoClient
        from pymongo.server_api import ServerApi
        import pymongo
        uri = "mongodb+srv://muneeb:seen123@muneeb.ibv9fe8.mongodb.net/?retryWrites=true&w=majority"
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client["Bank"]
        self.userAccountInfo = db["AccountInfo"]
    def accept(self):
        
        self.account["Loan"] = -int(self.loan_amount.text())
        print(self.account["Loan"])
        self.openLoanWindow()
    def openLoanWindow(self):
        
        self.loan_application.close()
        self.setupUi_loan(self.MainWindow)
        self.MainWindow.show()
        
    def reject(self):
        
        self.loan_application.close()
        self.MainWindow.close()
        
    def checkingAccount(self):
        pass 
    def savingsAccount(self):
        pass
    
app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()

bank = Bank(MainWindow=MainWindow)

sys.exit(app.exec_())
