
import contextlib
from doctest import master

from torch import matrix_power
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
import inspect
importlib.reload(intro_bank)
importlib.reload(login)
importlib.reload(create_account)


class MasterGUI(intro_bank.IntroPage, create_account.CreateAccount, login.Login, main.Home, loanApp.LoanApp, loan_window.LoanWindow):
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        self.setupUi_intro(self.MainWindow)
        self.MainWindow.show()
    def loginUser(self):
        self.login_button.clicked.connect(
            lambda: self.buttonclick(self.login_button))
        print("login")
        self.MainWindow.close()
        self.setupUi_login(self.MainWindow)
        self.MainWindow.show()

    def createUser(self):
        self.create_button.clicked.connect(
            lambda: self.buttonclick(self.create_button))
        print("create")
        self.MainWindow.close()
        self.setupUi_create(self.MainWindow)
        time.sleep(0.4)
        self.MainWindow.show()

    def openHomeWindow(self):
        self.MainWindow.close()
        Home.setupHome(self, self.MainWindow)

    def buttonclick(self, button:QtWidgets.QPushButton):
        print(button.objectName())
        # try:
        #     if self.timer2.isActive():
        #         QtWidgets.QMessageBox.critical(
        #             self.MainWindow,
        #             "Button Click",
        #             "Please wait five second for the transaction to complete."
        #         )
        #         time.sleep(2)
        # except:
        #     pass
        init_rect = button.geometry()
        new_rect = QtCore.QRect(*[int(x / 1.1)
                                for x in init_rect.getRect()])
        new_rect.translate(init_rect.x() - new_rect.x() + int(new_rect.width() // 20),
                            init_rect.y() - new_rect.y() + int(new_rect.height() // 20))
        button.setGeometry(new_rect)
        # Create a QTimer object
        self.timer1 = QtCore.QTimer()
        self.timer1.setSingleShot(True)  # Set the timer to fire only once transactions

        def reset_button_geometry():
            # Reset button geometry to original state
            button.setGeometry(init_rect)

        self.timer1.timeout.connect(reset_button_geometry)

        # Start the timer with a timeout of 2000 milliseconds (2 seconds)
        self.timer1.start(100)
        button.setEnabled(False)
        with contextlib.suppress(RuntimeError):
            # Create a QTimer object
            self.timer2 = QtCore.QTimer()

            # Set up the timeout function to enable the button after the specified duration
            self.timer2.timeout.connect(lambda: button.setEnabled(True)) if button else None

            # Start the timer
            self.timer2.start(5000)
    def accept(self):
        pass
    def reject(self):
        pass
    def createAccount(self):
        pass
    def checkCredentials(self):
        pass