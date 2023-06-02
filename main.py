
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from ui_main import DashBoard

# IMPORT FUNCTIONS
from ui_functions import *

class Home(QMainWindow, DashBoard):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 150, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.btn_page_1.clicked.connect(lambda: self.responsivePages.setCurrentWidget(self.mainDashBoard))

        # PAGE 2
        self.btn_page_2.clicked.connect(lambda: self.responsivePages.setCurrentWidget(self.card_page))

        # PAGE 3
        self.btn_page_3.clicked.connect(lambda: self.responsivePages.setCurrentWidget(self.Transactions))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = HomeWindow()
    sys.exit(app.exec_())
