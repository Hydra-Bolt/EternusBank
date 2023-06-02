
import DesignClass
import time
import sys
import random
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

    def createAccount(self):
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
            account = {accounts[i]: accounts_data[i] for i in range(len(accounts_data))}
            if account["Account Type"] != "Loan Account":
                account["Balance"] = 0
                account["Intereset Rate"] = 0.3
            # Check if the user already exists in the database
            result = list(self.userAccountInfo.find({"CNIC": info["CNIC"]}))
            if  result != []:
                update = {"$push": {"Accounts": account}}
                self.userAccountInfo.update_one({"CNIC": info["CNIC"]}, update=update)
            else:
                print('here')
                info.update({"Accounts": [account]})
                self.userAccountInfo.insert_one(info)

            self.openHomeWindow()


    def checkCredentials(self):
        filling_data = ["CNIC", "Account Name", "Password"]
        list_of_data = [self.cnic_line_edit.text(),self.account_edit_login.text(),self.password_login_edit.text()]
        infolist = [i == "" for i in list_of_data]
        if any(infolist):
            QtWidgets.QMessageBox(text=f"{filling_data[infolist.index(True)]} isnt filled")
            print(f"{filling_data[infolist.index(True)]} isnt filled")
        else:
            info = {filling_data[i]: list_of_data[i] for i in range(len(list_of_data))}
            self.output = self.userAccountInfo.find_one(info)
            print(self.output )
            if self.output  is None:
                print("DA UCK")
            else:
                self.openHomeWindow()
        
    def openHomeWindow(self):
        super().openHomeWindow()
        self.name_top.setText(f'Welcome, {self.output["Full Name"]}')
    def setupDB(self):
                
        from pymongo.mongo_client import MongoClient
        from pymongo.server_api import ServerApi
        import pymongo
        uri = "mongodb+srv://muneeb:seen123@muneeb.ibv9fe8.mongodb.net/?retryWrites=true&w=majority"
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client["Bank"]
        self.userAccountInfo = db["AccountInfo"]
        self.userAccountStatements = db["AccountStatements"]
        
app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()

bank = Bank(MainWindow=MainWindow)

sys.exit(app.exec_())
