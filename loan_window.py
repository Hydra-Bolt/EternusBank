from PyQt5 import QtCore, QtGui, QtWidgets

class LoanWindow:
    def setupUi_loan(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1091, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        # Create the main frame for the loan window
        self.mainframe_loan = QtWidgets.QFrame(self.centralwidget)
        self.mainframe_loan.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mainframe_loan.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe_loan.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe_loan.setObjectName("mainframe_loan")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainframe_loan)
        self.verticalLayout.setObjectName("verticalLayout")

        # Create the top bar frame
        self.topbar_loan = QtWidgets.QFrame(self.mainframe_loan)
        self.topbar_loan.setMaximumSize(QtCore.QSize(16777215, 40))
        self.topbar_loan.setStyleSheet("#topbar_loan{border:2px solid black;}")
        self.topbar_loan.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topbar_loan.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topbar_loan.setObjectName("topbar_loan")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.topbar_loan)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # Create labels for loan account and name
        self.loan_account = QtWidgets.QLabel(self.topbar_loan)
        self.loan_account.setStyleSheet('font: 18pt "Modern No. 20";color:green;')
        self.loan_account.setObjectName("loan_account")
        self.horizontalLayout_3.addWidget(self.loan_account)

        self.name_loan = QtWidgets.QLabel(self.topbar_loan)
        self.name_loan.setStyleSheet('font: 18pt "Modern No. 20";color:green;')
        self.name_loan.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.name_loan.setObjectName("name_loan")
        self.horizontalLayout_3.addWidget(self.name_loan)
        self.verticalLayout.addWidget(self.topbar_loan)

        # Create the principal amount frame
        self.principal_amount = QtWidgets.QFrame(self.mainframe_loan)
        self.principal_amount.setStyleSheet(
            "#principal_amount{border-bottom:2px dotted gray;}"
        )
        self.principal_amount.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.principal_amount.setFrameShadow(QtWidgets.QFrame.Raised)
        self.principal_amount.setObjectName("principal_amount")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.principal_amount)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Create the frame for principal label
        self.loan_frame = QtWidgets.QFrame(self.principal_amount)
        self.loan_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loan_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loan_frame.setObjectName("loan_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.loan_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Create the label for principal amount
        self.principal_label = QtWidgets.QLabel(self.loan_frame)
        self.principal_label.setStyleSheet('font: 30pt "Modern No. 20";')
        self.principal_label.setObjectName("principal_label")
        self.horizontalLayout_2.addWidget(self.principal_label)
        self.horizontalLayout.addWidget(self.loan_frame)

        # Create the label for total repayment amount
        self.total_repay = QtWidgets.QLabel(self.principal_amount)
        self.total_repay.setStyleSheet('font: 28pt "Modern No. 20";color:green;')
        self.total_repay.setAlignment(QtCore.Qt.AlignCenter)
        self.total_repay.setObjectName("total_repay")
        self.horizontalLayout.addWidget(self.total_repay)
        self.verticalLayout.addWidget(self.principal_amount)

        # Create the label for amount to be paid this month
        self.ammountToBePaid = QtWidgets.QLabel(self.mainframe_loan)
        self.ammountToBePaid.setStyleSheet('font: 28pt "Modern No. 20";color:red;')
        self.ammountToBePaid.setAlignment(QtCore.Qt.AlignCenter)
        self.ammountToBePaid.setObjectName("ammountToBePaid")
        self.verticalLayout.addWidget(self.ammountToBePaid)

        # Create the label for monthly amount
        self.month_amount = QtWidgets.QLabel(self.mainframe_loan)
        self.month_amount.setStyleSheet('font: 28pt "Modern No. 20";color:green;')
        self.month_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.month_amount.setObjectName("month_amount")
        self.verticalLayout.addWidget(self.month_amount)

        # Create the repay frame
        self.repay_frame = QtWidgets.QFrame(self.mainframe_loan)
        self.repay_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.repay_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.repay_frame.setObjectName("repay_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.repay_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # Create the label for "Repay your loan"
        self.repay = QtWidgets.QLabel(self.repay_frame)
        self.repay.setStyleSheet('font: 30pt "Modern No. 20";color:green;')
        self.repay.setObjectName("repay")
        self.verticalLayout_3.addWidget(self.repay)

        # Create the frame for repay edit and submit button
        self.repay_edit_frame = QtWidgets.QFrame(self.repay_frame)
        self.repay_edit_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.repay_edit_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.repay_edit_frame.setObjectName("repay_edit_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.repay_edit_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # Create the line edit for repay amount
        self.repay_edit = QtWidgets.QLineEdit(self.repay_edit_frame)
        self.repay_edit.setStyleSheet(
            'border:1.5px solid black;border-radius:5px;font: 26pt "Modern No. 20";padding:30px 12px;color:gray;'
        )
        self.repay_edit.setObjectName("repay_edit")
        self.repay_edit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{6}(?:\.[0-9]{2})?")))
        self.verticalLayout_4.addWidget(self.repay_edit)

        # Create the button for repay submit
        self.repay_submit = QtWidgets.QPushButton(self.repay_edit_frame)
        self.repay_submit.setStyleSheet(
            'border:2px solid black;border-radius:6px;font: 18pt "Modern No. 20";background-color:#28b44c;padding:6px 15px'
        )
        self.repay_submit.setObjectName("repay_submit")
        self.verticalLayout_4.addWidget(self.repay_submit, 0, QtCore.Qt.AlignHCenter)

        # Connect the repay_submit button to functions
        self.repay_submit.clicked.connect(self.repay_money)
        self.repay_submit.clicked.connect(lambda: self.buttonclick(self.repay_submit))

        self.verticalLayout_3.addWidget(self.repay_edit_frame)
        self.verticalLayout.addWidget(self.repay_frame)
        self.verticalLayout_5.addWidget(self.mainframe_loan)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loan_account.setText(_translate("MainWindow", "Loan Account"))
        self.name_loan.setText(_translate("MainWindow", "Welcome, Name here"))
        self.principal_label.setText(_translate("MainWindow", "Principal Amount:"))
        self.total_repay.setText(_translate("MainWindow", "= total amount"))
        self.ammountToBePaid.setText(
            _translate("MainWindow", "Amount to be paid this month")
        )
        self.month_amount.setText(_translate("MainWindow", "$3000"))
        self.repay.setText(_translate("MainWindow", "Repay your loan:"))
        self.repay_submit.setText(_translate("MainWindow", "Repay"))
