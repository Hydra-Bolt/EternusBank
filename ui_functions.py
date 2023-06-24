################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

## ==> GUI FILE
from ui_main import DashBoard
from PyQt5 import QtCore, QtWidgets, QtGui
class UIFunctions:

    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 72

            # SET MAX WIDTH
            if width == 72:
                widthExtended = maxExtend
                common_style = """
QPushButton {
    color: black;
    font: 13pt "Modern No. 20";
    background-color: rgb(255, 255, 255);
    border: 0px solid;
    text-align: left;
    padding-left: 25px;
}
QPushButton:hover {
    background-color: #f1fcf3;
}
"""
                self.btn_page_1.setText("Dashboard")
                self.btn_page_1.setStyleSheet(common_style)

                self.btn_page_2.setText("Card")
                self.btn_page_2.setStyleSheet(common_style)

                self.btn_page_3.setText("Transactions")
                self.btn_page_3.setStyleSheet(common_style)

                self.logout_button.setText("Logout")
                self.logout_button.setStyleSheet(common_style)
            else:
                widthExtended = standard
                self.btn_page_1.setText("")
                self.btn_page_2.setText("")
                self.btn_page_3.setText("")
                self.logout_button.setText("")

            # ANIMATION
            self.animation = QtCore.QPropertyAnimation(self.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
