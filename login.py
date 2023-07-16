from PyQt5 import QtCore, QtGui, QtWidgets


class Login:
    def setupUi_login(self, Login):
        Login.setObjectName("Login")
        Login.resize(1200, 600)
        Login.setMinimumSize(QtCore.QSize(1200, 600))
        Login.setMaximumSize(QtCore.QSize(1200, 600))
        Login.setStyleSheet("background-color: #f8f8f6;")
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.subframe = QtWidgets.QFrame(self.main_frame)
        self.subframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.subframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.subframe.setObjectName("subframe")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.subframe)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.subframe)
        self.label.setStyleSheet("* {\n"
                                 "    \n"
                                 "    font: 92pt \"Modern No. 20\";\n"
                                 "    color:green;\n"
                                 "    \n"
                                 "\n"
                                 "}")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.inputFieldsframe = QtWidgets.QFrame(self.subframe)
        self.inputFieldsframe.setMinimumSize(QtCore.QSize(600, 0))
        self.inputFieldsframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inputFieldsframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inputFieldsframe.setObjectName("inputFieldsframe")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.inputFieldsframe)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cnic_label_login = QtWidgets.QLabel(self.inputFieldsframe)
        
        self.cnic_label_login.setStyleSheet("* {\n"
                                            "    font: 12pt \"Modern No. 20\";\n"
                                            "    color:green;\n"
                                            "    padding:0px 5px;\n"
                                            "}")
        self.cnic_label_login.setObjectName("cnic_label_login")
        self.verticalLayout_3.addWidget(self.cnic_label_login)
        self.cnic_line_edit = QtWidgets.QLineEdit(self.inputFieldsframe)
        self.cnic_line_edit.setStyleSheet("* {\n"
                                          "    font: 12pt \"Modern No. 20\";\n"
                                          "    color:green;\n"
                                          "    padding:3px 10px;\n"
                                          "    border:1px solid darkgreen;\n"
                                          "    border-radius:5px;\n"
                                          "}")
        self.cnic_line_edit.setObjectName("cnic_line_edit")
        self.cnic_line_edit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{13}"), self.cnic_line_edit))
        self.verticalLayout_3.addWidget(self.cnic_line_edit)
        self.phone_number_login_label = QtWidgets.QLabel(self.inputFieldsframe)
        self.phone_number_login_label.setStyleSheet("* {\n"
                                               "    font: 12pt \"Modern No. 20\";\n"
                                               "    color:green;\n"
                                               "    padding:0px 5px;\n"
                                               "}")
        self.phone_number_login_label.setObjectName("phone_number_login_label")
        self.verticalLayout_3.addWidget(self.phone_number_login_label)
        self.phone_number_login = QtWidgets.QLineEdit(self.inputFieldsframe)
        self.phone_number_login.setStyleSheet("* {\n"
                                              "    font: 12pt \"Modern No. 20\";\n"
                                              "    color:green;\n"
                                              "    padding:3px 10px;\n"
                                              "    border:1px solid darkgreen;\n"
                                              "    border-radius:5px;\n"
                                              "}")
        self.phone_number_login.setObjectName("phone_number_login")
        self.phone_number_login.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("(\+92|0)?3[0-9]{2}-?[0-9]{7}"), self.phone_number_login))
        self.verticalLayout_3.addWidget(self.phone_number_login)
        self.password_login = QtWidgets.QLabel(self.inputFieldsframe)
        self.password_login.setStyleSheet("* {\n"
                                          "    font: 12pt \"Modern No. 20\";\n"
                                          "    color:green;\n"
                                          "    padding:0px 5px;\n"
                                          "}")
        self.password_login.setObjectName("password_login")
        self.verticalLayout_3.addWidget(self.password_login)
        self.password_login_edit = QtWidgets.QLineEdit(self.inputFieldsframe)
        self.password_login_edit.setStyleSheet("* {\n"
                                               "    font: 12pt \"Modern No. 20\";\n"
                                               "    color:green;\n"
                                               "    padding:3px 10px;\n"
                                               "    border:1px solid darkgreen;\n"
                                               "    border-radius:5px;\n"
                                               "}")
        self.password_login_edit.setObjectName("password_login_edit")
        self.password_login_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout_3.addWidget(self.password_login_edit)
        self.buttonframe = QtWidgets.QFrame(self.inputFieldsframe)
        self.buttonframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonframe.setObjectName("buttonframe")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.buttonframe)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.submit_login = QtWidgets.QPushButton(self.buttonframe)
        self.submit_login.setMaximumSize(QtCore.QSize(200, 16777215))
        self.submit_login.setStyleSheet("* {\n"
                                        "    font: 20pt \"Modern No. 20\";\n"
                                        "    color:green;\n"
                                        "    padding:3px 20px;\n"
                                        "    border:2px solid darkgreen;\n"
                                        "    border-radius:5px;\n"
                                        "}")
        self.submit_login.setObjectName("submit_login")
        self.submit_login.clicked.connect(self.checkCredentials)
        self.horizontalLayout_2.addWidget(self.submit_login)
        self.verticalLayout_3.addWidget(self.buttonframe)
        self.verticalLayout_2.addWidget(self.inputFieldsframe)
        self.verticalLayout.addWidget(self.subframe)
        self.horizontalLayout.addWidget(self.main_frame)
        Login.setCentralWidget(self.centralwidget)
        Login.setWindowTitle("Login")

        self.setUI_login(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def setUI_login(self, Login):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Login", "Great to have you back."))
        self.cnic_label_login.setText(
            _translate("Login", "CNIC (Without dashes) :"))
        self.cnic_line_edit.setWhatsThis(_translate(
            "Login", "Input Computerized National Identity Card Number here"))
        self.cnic_line_edit.setPlaceholderText(
            _translate("Login", "XXXXXXXXXXXXX"))
        self.phone_number_login_label.setText(_translate("Login", "Phone Number:"))
        self.phone_number_login.setPlaceholderText(
            _translate("Login", "+92XXXXXXXXXX"))
        self.password_login.setText(_translate("Login", "Password:"))
        self.password_login_edit.setPlaceholderText(
            _translate("Login", "XXXXXXXXXXX"))
        self.submit_login.setText(_translate("Login", "Login"))
        
    def checkCredentials(self):
        pass