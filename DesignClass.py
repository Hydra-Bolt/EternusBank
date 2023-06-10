
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
        self.login_button.clicked.connect(lambda: self.buttonclick(self.login_button))
        self.MainWindow.close()
        self.setupUi_login(self.MainWindow)
        self.MainWindow.show()
        
    def createUser(self):
        self.create_button.clicked.connect(lambda: self.buttonclick(self.create_button))
        self.MainWindow.close()
        self.setupUi_create(self.MainWindow)
        time.sleep(0.4)
        self.MainWindow.show()
    def openHomeWindow(self):
        self.MainWindow.close()
        Home.__init__(self)
    def buttonclick(self, button):
        init_rect = button.geometry()
        new_rect = QtCore.QRect(*[int(x / 1.1) for x in init_rect.getRect()])
        new_rect.translate(init_rect.x() - new_rect.x() + int(new_rect.width() // 20),
                        init_rect.y() - new_rect.y() + int(new_rect.height() // 20))
        button.setGeometry(new_rect)

        # Create a QTimer object
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)  # Set the timer to fire only once

        def reset_button_geometry():
            button.setGeometry(init_rect)  # Reset button geometry to original state

        self.timer.timeout.connect(reset_button_geometry)

        # Start the timer with a timeout of 2000 milliseconds (2 seconds)
        self.timer.start(100)