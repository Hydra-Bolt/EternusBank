
import login
import create_account
import time
import sys
import importlib
from main import Home
import intro_bank
import loan_window

from PyQt5 import QtCore, QtGui, QtWidgets
import main
import loanApp
importlib.reload(intro_bank)
importlib.reload(login)
importlib.reload(create_account)


class MasterGUI(intro_bank.IntroPage, create_account.Ui_CreateAccount, login.Ui_Login, main.Home, loanApp.LoanApp,loan_window.Loan):
    def __init__(self):
        intro_bank.IntroPage.__init__(self)
    def loginUser(self):
        self.MainWindow.close()
        self.setupUi_login(self.MainWindow)
        self.MainWindow.show()
        
    def createUser(self):
        self.MainWindow.close()
        self.setupUi_create(self.MainWindow)
        time.sleep(0.4)
        self.MainWindow.show()
    def openHomeWindow(self):
        self.MainWindow.close()
        Home.__init__(self)
    