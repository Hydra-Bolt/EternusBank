
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
        self.btn_page_2.clicked.connect(lambda: self.responsivePages.setCurrentWidget(self.cardpage))

        # PAGE 3
        self.btn_page_3.clicked.connect(lambda: self.responsivePages.setCurrentWidget(self.Transactions))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##
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
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Home()
    sys.exit(app.exec_())
