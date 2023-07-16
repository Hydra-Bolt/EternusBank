
import platform
from PyQt5 import QtCore,QtGui,QtWidgets
from abc import ABC, abstractmethod
# GUI FILE
from ui_main import DashBoard

# IMPORT FUNCTIONS
from ui_functions import *
# class CommonMeta(type(ABC), type(QtWidgets.QMainWindow), type(DashBoard)):
#     pass

class Home(DashBoard):
    def setupHome(self, MainWindow):
        self.MainWindow = MainWindow
        self.setupDashboard(self.MainWindow)
        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 150, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.btn_page_1.clicked.connect(lambda: self.responsivePages.setCurrentWidget(self.mainDashBoard))

        # PAGE 2
        self.btn_page_2.clicked.connect(lambda: self.responsivePages.setCurrentWidget(self.cardpage))

        # PAGE 3
        
        self.btn_page_3.clicked.connect(lambda: self.responsivePages.setCurrentWidget(self.Transactions))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.MainWindow.show()
        ## ==> END ##
    def setupVars(self):
        self.setupDashboard(self)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Home()
    sys.exit(app.exec_())
