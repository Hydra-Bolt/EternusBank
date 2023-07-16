from PyQt5 import QtCore, QtGui, QtWidgets

class CreateAccount:
    def setupUi_create(self, CreateAccount):
        CreateAccount.setObjectName("CreateAccount")
        CreateAccount.resize(1200, 600)
        CreateAccount.setMinimumSize(QtCore.QSize(1200, 0))
        CreateAccount.setMaximumSize(QtCore.QSize(1200, 600))
        CreateAccount.setStyleSheet("background-color: #f8f8f6;")
        
        
        self.centralwidget = QtWidgets.QWidget(CreateAccount)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.message = QtWidgets.QLabel(self.frame_2)
        self.message.setStyleSheet("QLabel {\n"
                                   "    font: 58pt \"Modern No. 20\";\n"
                                   "    color:green;\n"
                                   "\n"
                                   "}")
        self.message.setObjectName("message")
        self.verticalLayout_2.addWidget(self.message)
        self.label_frames = QtWidgets.QFrame(self.frame_2)
        self.label_frames.setMinimumSize(QtCore.QSize(350, 0))
        self.label_frames.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_frames.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_frames.setObjectName("label_frames")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.label_frames)
        self.verticalLayout.setObjectName("verticalLayout")
        self.full_name_label = QtWidgets.QLabel(self.label_frames)
        self.full_name_label.setMinimumSize(QtCore.QSize(500, 0))
        self.full_name_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.full_name_label.setStyleSheet("* {\n"
                                           "    font: 12pt \"Modern No. 20\";\n"
                                           "    color:green;\n"
                                           "    padding:0px 5px;\n"
                                           "}")
        self.full_name_label.setObjectName("full_name_label")
        self.verticalLayout.addWidget(self.full_name_label)
        self.fullname = QtWidgets.QLineEdit(self.label_frames)
        self.fullname.setMinimumSize(QtCore.QSize(0, 0))
        self.fullname.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.fullname.setStyleSheet("* {\n"
                                    "    font: 12pt \"Modern No. 20\";\n"
                                    "    color:green;\n"
                                    "    padding:3px 10px;\n"
                                    "    border:1px solid darkgreen;\n"
                                    "    border-radius:5px;\n"
                                    "}")
        self.fullname.setObjectName("fullname")
        self.fullname.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[A-Za-z ]+"), self.fullname))
        self.verticalLayout.addWidget(self.fullname)
        self.phone_number_label = QtWidgets.QLabel(self.label_frames)
        self.phone_number_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.phone_number_label.setStyleSheet("* {\n"
                                              "    font: 12pt \"Modern No. 20\";\n"
                                              "    color:green;\n"
                                              "    padding:0px 5px;\n"
                                              "}")
        self.phone_number_label.setObjectName("phone_number_label")
        self.verticalLayout.addWidget(self.phone_number_label)
        self.phone_number = QtWidgets.QLineEdit(self.label_frames)
        self.phone_number.setStyleSheet("* {\n"
                                        "    font: 12pt \"Modern No. 20\";\n"
                                        "    color:green;\n"
                                        "    padding:3px 10px;\n"
                                        "    border:1px solid darkgreen;\n"
                                        "    border-radius:5px;\n"
                                        "}")
        self.phone_number.setObjectName("phone_number")
        self.phone_number.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("(\+92|0)?3[0-9]{2}-?[0-9]{7}"), self.phone_number))
        self.verticalLayout.addWidget(self.phone_number)
        self.cnic_label = QtWidgets.QLabel(self.label_frames)
        self.cnic_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.cnic_label.setStyleSheet("* {\n"
                                      "    font: 12pt \"Modern No. 20\";\n"
                                      "    color:green;\n"
                                      "    padding:0px 5px;\n"
                                      "}")
        self.cnic_label.setObjectName("cnic_label")
        self.verticalLayout.addWidget(self.cnic_label)
        self.cnic = QtWidgets.QLineEdit(self.label_frames)
        self.cnic.setStyleSheet("* {\n"
                                "    font: 12pt \"Modern No. 20\";\n"
                                "    color:green;\n"
                                "    padding:3px 10px;\n"
                                "    border:1px solid darkgreen;\n"
                                "    border-radius:5px;\n"
                                "}")
        self.cnic.setObjectName("cnic")
        self.cnic.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{13}"), self.cnic))
        self.verticalLayout.addWidget(self.cnic)
        self.password_create_label = QtWidgets.QLabel(self.label_frames)
        self.password_create_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.password_create_label.setStyleSheet("* {\n"
                                              "    font: 12pt \"Modern No. 20\";\n"
                                              "    color:green;\n"
                                              "    padding:0px 5px;\n"
                                              "}")
        self.password_create_label.setObjectName("password_create_label")
        self.verticalLayout.addWidget(self.password_create_label)
        self.password_create = QtWidgets.QLineEdit(self.label_frames)
        self.password_create.setStyleSheet("* {\n"
                                        "    font: 12pt \"Modern No. 20\";\n"
                                        "    color:green;\n"
                                        "    padding:3px 10px;\n"
                                        "    border:1px solid darkgreen;\n"
                                        "    border-radius:5px;\n"
                                        "}")
        self.password_create.setObjectName("password_create")
        self.password_create.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout.addWidget(self.password_create)
        self.account_type_label = QtWidgets.QLabel(self.label_frames)
        self.account_type_label.setStyleSheet("* {\n"
                                              "    font: 12pt \"Modern No. 20\";\n"
                                              "    color:green;\n"
                                              "    padding:0px 5px;\n"
                                              "}")
        self.account_type_label.setObjectName("account_type_label")
        self.verticalLayout.addWidget(self.account_type_label)
        self.accountype = QtWidgets.QComboBox(self.label_frames)
        self.accountype.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.accountype.setStyleSheet("* {\n"
                                      "    font: 12pt \"Modern No. 20\";\n"
                                      "    color:green;\n"
                                      "    padding:3px 10px;\n"
                                      "    border:1px solid darkgreen;\n"
                                      "    border-radius:5px;\n"
                                      "}")
        self.accountype.setObjectName("accountype")
        self.accountype.addItem("Checking Account")
        self.accountype.addItem("Savings Account")
        self.accountype.addItem("Loan Account")
        self.verticalLayout.addWidget(self.accountype)
        self.submit_buttonframe = QtWidgets.QFrame(self.label_frames)
        self.submit_buttonframe.setMinimumSize(QtCore.QSize(0, 122))
        self.submit_buttonframe.setMaximumSize(QtCore.QSize(16777215, 70))
        self.submit_buttonframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.submit_buttonframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.submit_buttonframe.setObjectName("submit_buttonframe")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.submit_buttonframe)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.submit_button_create = QtWidgets.QPushButton(self.submit_buttonframe)
        self.submit_button_create.setMaximumSize(QtCore.QSize(200, 16777215))
        self.submit_button_create.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit_button_create.setStyleSheet("* {\n"
                                      "    font: 20pt \"Modern No. 20\";\n"
                                      "    color:green;\n"
                                      "    padding:3px 20px;\n"
                                      "    border:2px solid darkgreen;\n"
                                      "    border-radius:5px;\n"
                                      "}")
        self.submit_button_create.setObjectName("submit_button_create")
        self.verticalLayout_3.addWidget(self.submit_button_create)
        self.submit_button_create.clicked.connect(self.createAccount)
        # self.submit_button_create.clicked.connect(lambda:self.buttonclick(self.submit_button_create))
        self.verticalLayout.addWidget(
            self.submit_buttonframe, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(
            self.label_frames, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        CreateAccount.setWindowTitle("Account Creation")
        CreateAccount.setCentralWidget(self.centralwidget)

        self.setUI_create(CreateAccount)
        QtCore.QMetaObject.connectSlotsByName(CreateAccount)

    def setUI_create(self, CreateAccount):
        _translate = QtCore.QCoreApplication.translate
        self.message.setText(_translate(
            "CreateAccount", "Welcome, Happy to have you join us."))
        self.full_name_label.setText(_translate("CreateAccount", "Full Name:"))
        self.fullname.setPlaceholderText(
            _translate("CreateAccount", "John Doe"))
        self.phone_number_label.setText(_translate(
            "CreateAccount", "Phone Number"))
        self.phone_number.setPlaceholderText(
            _translate("CreateAccount", "+92XXXXXXXXXX"))
        self.cnic_label.setText(_translate("CreateAccount", "CNIC:"))
        self.cnic.setPlaceholderText(_translate(
            "CreateAccount", "XXXXX-XXXXXXX-X"))
        self.password_create_label.setText(
            _translate("CreateAccount", "Password:"))
        self.password_create.setPlaceholderText(
            _translate("CreateAccount", "XXXXXXXXXX"))
        self.account_type_label.setText(_translate(
            "CreateAccount", "Which type of account would you like?"))
        self.accountype.setItemText(0, _translate(
            "CreateAccount", "Savings Account"))
        self.accountype.setItemText(
            1, _translate("CreateAccount", "Loan Account"))
        self.accountype.setItemText(2, _translate(
            "CreateAccount", "Checking Account"))
        self.submit_button_create.setText(_translate("CreateAccount", "Submit"))


    def createAccount(self):
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateAccount = QtWidgets.QMainWindow()
    ui = Ui_CreateAccount()
    ui.setupUi_create(CreateAccount)
    CreateAccount.show()
    sys.exit(app.exec_())
