from PyQt5 import QtCore, QtGui, QtWidgets

class Loan:
    def setupUi_loan(self, MainWindow):
        # Setup the UI for the loan application window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        # Create the main frame for the loan application window
        self.mainframe_loan = QtWidgets.QFrame(self.centralwidget)
        self.mainframe_loan.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mainframe_loan.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe_loan.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe_loan.setObjectName("mainframe_loan")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainframe_loan)
        self.verticalLayout.setObjectName("verticalLayout")

        # Create the top bar frame for the loan application window
        self.topbar_loan = QtWidgets.QFrame(self.mainframe_loan)
        self.topbar_loan.setMaximumSize(QtCore.QSize(16777215, 40))
        self.topbar_loan.setStyleSheet("#topbar_loan{border:2px solid black;}")
        self.topbar_loan.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topbar_loan.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topbar_loan.setObjectName("topbar_loan")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.topbar_loan)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # Create labels for the loan account and user name in the top bar
        self.loan_account = QtWidgets.QLabel(self.topbar_loan)
        self.loan_account.setStyleSheet("font: 18pt \"Modern No. 20\";color:green;")
        self.loan_account.setObjectName("loan_account")
        self.horizontalLayout_3.addWidget(self.loan_account)
        self.name_loan = QtWidgets.QLabel(self.topbar_loan)
        self.name_loan.setStyleSheet("font: 18pt \"Modern No. 20\";color:green;")
        self.name_loan.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.name_loan.setObjectName("name_loan")
        self.horizontalLayout_3.addWidget(self.name_loan)
        self.verticalLayout.addWidget(self.topbar_loan)

        # Create the frame for displaying the principal amount
        self.principal_amount = QtWidgets.QFrame(self.mainframe_loan)
        self.principal_amount.setStyleSheet("#principal_amount{border-bottom:2px dotted gray;}")
        self.principal_amount.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.principal_amount.setFrameShadow(QtWidgets.QFrame.Raised)
        self.principal_amount.setObjectName("principal_amount")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.principal_amount)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Create the label for the principal amount
        self.principal_label = QtWidgets.QLabel(self.principal_amount)
        self.principal_label.setStyleSheet("font: 30pt \"Modern No. 20\";")
        self.principal_label.setObjectName("principal_label")
        self.verticalLayout_2.addWidget(self.principal_label)

        # Create the frame for displaying loan information (loan taken, interest, total repayment)
        self.loan_frame = QtWidgets.QFrame(self.principal_amount)
        self.loan_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loan_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loan_frame.setObjectName("loan_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.loan_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Create labels for displaying loan taken, interest, and total repayment
        self.loan_taken = QtWidgets.QLabel(self.loan_frame)
        self.loan_taken.setStyleSheet("font: 28pt \"Modern No. 20\";color:green;")
        self.loan_taken.setAlignment(QtCore.Qt.AlignCenter)
        self.loan_taken.setObjectName("loan_taken")
        self.horizontalLayout_2.addWidget(self.loan_taken)
        self.interest = QtWidgets.QLabel(self.loan_frame)
        self.interest.setStyleSheet("font: 28pt \"Modern No. 20\";color:red;")
        self.interest.setAlignment(QtCore.Qt.AlignCenter)
        self.interest.setObjectName("interest")
        self.horizontalLayout_2.addWidget(self.interest)
        self.total_repay = QtWidgets.QLabel(self.loan_frame)
        self.total_repay.setStyleSheet("font: 28pt \"Modern No. 20\";color:green;")
        self.total_repay.setAlignment(QtCore.Qt.AlignCenter)
        self.total_repay.setObjectName("total_repay")
        self.horizontalLayout_2.addWidget(self.total_repay)

        self.verticalLayout_2.addWidget(self.loan_frame)
        self.verticalLayout.addWidget(self.principal_amount)

        # Create the frame for loan repayment
        self.repay_frame = QtWidgets.QFrame(self.mainframe_loan)
        self.repay_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.repay_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.repay_frame.setObjectName("repay_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.repay_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # Create label for displaying repayment instructions
        self.repay = QtWidgets.QLabel(self.repay_frame)
        self.repay.setStyleSheet("font: 30pt \"Modern No. 20\";color:green;")
        self.repay.setObjectName("repay")
        self.verticalLayout_3.addWidget(self.repay)

        # Create frame for the repayment input field and submit button
        self.repay_edit_frame = QtWidgets.QFrame(self.repay_frame)
        self.repay_edit_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.repay_edit_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.repay_edit_frame.setObjectName("repay_edit_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.repay_edit_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # Create the input field for entering the repayment amount
        self.repay_edit = QtWidgets.QLineEdit(self.repay_edit_frame)
        self.repay_edit.setStyleSheet("border:1.5px solid black;border-radius:5px;font: 26pt \"Modern No. 20\";padding:30px 12px;color:gray;")
        self.repay_edit.setObjectName("repay_edit")
        self.verticalLayout_4.addWidget(self.repay_edit)

        # Create the submit button for repaying the loan
        self.repay_submit = QtWidgets.QPushButton(self.repay_edit_frame)
        self.repay_submit.setStyleSheet("border:2px solid black;border-radius:6px;font: 18pt \"Modern No. 20\";background-color:#28b44c;padding:6px 15px")
        self.repay_submit.setObjectName("repay_submit")
        self.verticalLayout_4.addWidget(self.repay_submit, 0, QtCore.Qt.AlignHCenter)

        self.verticalLayout_3.addWidget(self.repay_edit_frame)
        self.verticalLayout.addWidget(self.repay_frame)

        self.verticalLayout_5.addWidget(self.mainframe_loan)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi_loan(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi_loan(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Loan Account"))
        self.loan_account.setText(_translate("MainWindow", "Loan Account"))
        self.name_loan.setText(_translate("MainWindow", "Welcome, Name here"))
        self.principal_label.setText(_translate("MainWindow", "Principal Amount:"))
        self.loan_taken.setText(_translate("MainWindow", "$3000"))
        self.interest.setText(_translate("MainWindow", "+ interest"))
        self.total_repay.setText(_translate("MainWindow", "= total amount"))
        self.repay.setText(_translate("MainWindow", "Repay your loan:"))
        self.repay_edit.setText(_translate("MainWindow", "$"))
        self.repay_submit.setText(_translate("MainWindow", "Repay"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Loan()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
