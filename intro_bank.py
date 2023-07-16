
from PyQt5 import QtCore, QtGui, QtWidgets

class IntroPage:
    
    def setupUi_intro(self, MainWindow: QtWidgets.QMainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(1200, 800)
        # MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("* {\n"
                                 "background-color:#f8f8f6\n"
                                 "\n"
                                 "}")
        # self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.title = QtWidgets.QLabel(self.frame_2)
        self.title.setStyleSheet("* {\n"
                                 "    color:green;\n"
                                 "    font: 36pt \"Modern No. 20\";\n"
                                 "\n"
                                 "        padding:12px;\n"
                                 "\n"
                                 "}")
        self.title.setObjectName("title")
        self.verticalLayout_4.addWidget(self.title)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4.addWidget(self.frame_4)
        self.slogan = QtWidgets.QLabel(self.frame_2)
        self.slogan.setStyleSheet("* {\n"
                                  "    font-weight:bold;\n"
                                  "    font: 24pt \"Modern No. 20\";\n"
                                  "    color:green;\n"
                                  "}")
        self.slogan.setObjectName("slogan")
        self.verticalLayout_4.addWidget(self.slogan)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("* {\n"
                                 "    font-weight:bold;\n"
                                 "    font: 12pt \"Modern No. 20\";\n"
                                 "    color:green;\n"
                                 "}")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("background-repeat: no-repeat;\n"
                                   "background-position: center;\n"
                                   "background-image: url(icons/logo.png);\n")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)
        self.space = QtWidgets.QFrame(self.centralwidget)
        self.space.setMaximumSize(QtCore.QSize(16777215, 70))
        self.space.setStyleSheet("# {\n"
                                 "    background-color: rgb(248, 248, 248);\n"
                                 "\n"
                                 "}")
        self.space.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.space.setFrameShadow(QtWidgets.QFrame.Raised)
        self.space.setObjectName("space")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.space)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addWidget(self.space)
        self.slogan_frame = QtWidgets.QFrame(self.centralwidget)
        self.slogan_frame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.slogan_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slogan_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slogan_frame.setObjectName("slogan_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.slogan_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.create_login_frame = QtWidgets.QFrame(self.slogan_frame)
        self.create_login_frame.setMinimumSize(QtCore.QSize(0, 200))
        self.create_login_frame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.create_login_frame.setStyleSheet("QPushButton {\n"
                                              "    width:12px;\n"
                                              "\n"
                                              "}")
        self.create_login_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.create_login_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.create_login_frame.setObjectName("create_login_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(
            self.create_login_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.create_button = QtWidgets.QPushButton(self.create_login_frame)
        self.create_button.setStyleSheet("QPushButton {\n"
                                         "    \n"
                                         "    font: 12pt \"Modern No. 20\";\n"
                                         "    color: #02ae1a;\n"
                                         "    border-radius: 15px;\n"
                                         "    background-color:#f8f8f6;\n"
                                         "    border: 0.5px solid black;\n"
                                         "    padding:12px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    color:#00c61c\n"
                                         "}\n"
                                         "")
        self.create_button.setObjectName("create_button")
        # self.create_button.clicked.connect(lambda: self.buttonclick(self.create_button))
        self.horizontalLayout_2.addWidget(self.create_button)
        self.login_button = QtWidgets.QPushButton(self.create_login_frame)
        self.login_button.setStyleSheet("QPushButton {\n"
                                        "    \n"
                                        "    font: 12pt \"Modern No. 20\";\n"
                                        "    color: #02ae1a;\n"
                                        "    border-radius: 15px;\n"
                                        "    background-color:#f8f8f6;\n"
                                        "    border: 0.5px solid black;\n"
                                        "    padding:12px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    color:#00c61c\n"
                                        "}\n"
                                        "")
        self.login_button.setObjectName("login_button")
        # self.login_button.clicked.connect(lambda: self.buttonclick(self.login_button))
        self.horizontalLayout_2.addWidget(self.login_button)
        self.verticalLayout_2.addWidget(self.create_login_frame)
        self.verticalLayout.addWidget(self.slogan_frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.create_button.clicked.connect(self.createUser)
        self.login_button.clicked.connect(self.loginUser)
        self.setUi_intro(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setUi_intro(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome to Eternus Banking"))
        self.title.setText(_translate("MainWindow", "Eternus Banking"))
        self.slogan.setText(_translate(
            "MainWindow", "Where your financial future lasts forever."))
        self.label.setText(_translate("MainWindow", "Join us today and secure your financial future with Bank Eternus. Create an account or log in now to take the\n"
                                      "first step towards everlasting financial stability."))
        self.create_button.setText(_translate("MainWindow", "Create Account"))
        self.login_button.setText(_translate("MainWindow", "Login"))

    def createUser(self):
        pass
    def loginUser(self):
        pass
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = IntroPage()
    ui.setupUi_intro(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
