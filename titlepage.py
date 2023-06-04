from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class IntroPage(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(984, 668)
        MainWindow.setStyleSheet(u"* {\n"
                                 "background-color:white;\n"
                                 "}\n"
                                 "")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setStyleSheet(u"* {\n"
                                 "	color:green;\n"
                                 "	font: 36pt \"Modern No. 20\";\n"
                                 "\n"
                                 "		padding:12px;\n"
                                 "\n"
                                 "}")

        self.verticalLayout.addWidget(self.title)

        self.space = QFrame(self.centralwidget)
        self.space.setObjectName(u"space")
        self.space.setMaximumSize(QSize(16777215, 100))
        self.space.setStyleSheet(u"# {\n"
                                 "	background-color: rgb(248, 248, 248);\n"
                                 "\n"
                                 "}")
        self.space.setFrameShape(QFrame.StyledPanel)
        self.space.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.space)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addWidget(self.space)

        self.slogan_frame = QFrame(self.centralwidget)
        self.slogan_frame.setObjectName(u"slogan_frame")
        self.slogan_frame.setFrameShape(QFrame.StyledPanel)
        self.slogan_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.slogan_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.slogan = QLabel(self.slogan_frame)
        self.slogan.setObjectName(u"slogan")
        self.slogan.setStyleSheet(u"* {\n"
                                  "	font-weight:bold;\n"
                                  "	font: 24pt \"Modern No. 20\";\n"
                                  "	color:green;\n"
                                  "}")

        self.verticalLayout_2.addWidget(self.slogan)

        self.verticalLayout.addWidget(self.slogan_frame)

        self.create_login_frame = QFrame(self.centralwidget)
        self.create_login_frame.setObjectName(u"create_login_frame")
        self.create_login_frame.setMinimumSize(QSize(0, 200))
        self.create_login_frame.setStyleSheet(u"QPushButton {\n"
                                              "	width:12px;\n"
                                              "\n"
                                              "}")
        self.create_login_frame.setFrameShape(QFrame.StyledPanel)
        self.create_login_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.create_login_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.create_button = QPushButton(self.create_login_frame)
        self.create_button.setObjectName(u"create_button")
        self.create_button.setStyleSheet(u"QPushButton {\n"
                                         "	\n"
                                         "	font: 12pt \"Modern No. 20\";\n"
                                         "	color: #02ae1a;\n"
                                         "	border-radius: 15px;\n"
                                         "	background-color:#f8f8f6;\n"
                                         "	border: 0.5px solid black;\n"
                                         "	padding:12px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "	color:#00c61c\n"
                                         "}\n"
                                         "")

        self.gridLayout.addWidget(self.create_button, 0, 0, 1, 1)

        self.login_button = QPushButton(self.create_login_frame)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setStyleSheet(u"QPushButton {\n"
                                        "	\n"
                                        "	font: 12pt \"Modern No. 20\";\n"
                                        "	color: #02ae1a;\n"
                                        "	border-radius: 15px;\n"
                                        "	background-color:#f8f8f6;\n"
                                        "	border: 0.5px solid black;\n"
                                        "	padding:12px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "	color:#00c61c\n"
                                        "}\n"
                                        "")

        self.gridLayout.addWidget(self.login_button, 1, 1, 1, 1)

        self.verticalLayout.addWidget(self.create_login_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate(
            "MainWindow", u"Eternus Banking", None))
        self.slogan.setText(QCoreApplication.translate(
            "MainWindow", u"Where your financial future lasts forever.", None))
        self.create_button.setText(QCoreApplication.translate(
            "MainWindow", u"Create Account", None))
        self.login_button.setText(
            QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi
