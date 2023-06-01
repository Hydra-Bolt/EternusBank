
import DesignClass
import time
import sys
import importlib
from PyQt5 import QtCore, QtGui, QtWidgets


class Bank(DesignClass.MasterGUI):
    
    def __init__(self, MainWindow: QtWidgets.QMainWindow) -> None:
        super().__init__()
        self.setupDB()
        self.MainWindow = MainWindow
        self.setupUi_intro(self.MainWindow)
        self.MainWindow.setWindowIcon(QtGui.QIcon('logo.png'))
        self.MainWindow.show()

    def createAccount(self):
        filling_data = ["Full Name", "Account Name", "CNIC", "Password", "Account Type"]
        list_of_data = [self.fullname.text(),self.account_name.text(), self.cnic.text(), self.password_create.text(),self.accountype.currentText()]
        infolist = [i == "" for i in list_of_data]
        if any(infolist):
            print(f"{filling_data[infolist.index(True)]} isnt filled")
        else:
            info = {filling_data[i]: list_of_data[i] for i in range(len(list_of_data))}
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
