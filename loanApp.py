from PyQt5 import QtCore, QtGui, QtWidgets


class LoanApp:
    def setupLoanApp(self, Loan):
        # Set up the main window properties
        Loan.setObjectName("Loan")
        Loan.resize(1000, 500)
        Loan.setMinimumSize(QtCore.QSize(1000, 500))
        Loan.setStyleSheet("background-color:white;")
        
        # Create the vertical layout for the main window
        self.verticalLayout = QtWidgets.QVBoxLayout(Loan)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Add a welcome label to the vertical layout
        self.welcome_loan = QtWidgets.QLabel(Loan)
        self.welcome_loan.setStyleSheet("font: 26pt \"Modern No. 20\";")
        self.welcome_loan.setObjectName("welcome_loan")
        self.verticalLayout.addWidget(self.welcome_loan)
        
        # Add a question label to the vertical layout
        self.ask_loan = QtWidgets.QLabel(Loan)
        self.ask_loan.setStyleSheet("font: 16pt \"Modern No. 20\";")
        self.ask_loan.setObjectName("ask_loan")
        self.verticalLayout.addWidget(self.ask_loan)
        
        # Add a line edit for loan amount input to the vertical layout
        self.loan_amount = QtWidgets.QLineEdit(Loan)
        self.loan_amount.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{1,6}(?:\.[0-9]{1,2})?")))
        self.loan_amount.setStyleSheet("font: 16pt \"Modern No. 20\";border-radius:5px;border:1px solid black;padding:6px")
        self.loan_amount.setObjectName("loan_amount")
        self.verticalLayout.addWidget(self.loan_amount)
        
        # Add a scale widget for the amount of months to pay back the loan
        self.months_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.months_slider.setObjectName("months_slider")
        self.months_slider.setMinimum(1)
        self.months_slider.setMaximum(60)  # Adjust the maximum as per your requirements
        self.months_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.months_slider.setTickInterval(1)
        self.months_slider.valueChanged.connect(self.slider_change)
        self.verticalLayout.addWidget(self.months_slider)
        
        self.months_loan = QtWidgets.QLabel(Loan)
        self.months_loan.setMaximumHeight(70)
        self.months_loan.setStyleSheet("font: 16pt \"Modern No. 20\";")
        self.months_loan.setObjectName("ask_loan")
        self.verticalLayout.addWidget(self.months_loan)
        
        # Add an OK/Cancel button box to the vertical layout
        self.okcancel = QtWidgets.QDialogButtonBox(Loan)
        self.okcancel.setMinimumSize(QtCore.QSize(0, 0))
        self.okcancel.setStyleSheet("font: 16pt \"Modern No. 20\";border-radius:5px;border:1px solid black;padding:6px")
        self.okcancel.setOrientation(QtCore.Qt.Horizontal)
        self.okcancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.okcancel.setObjectName("okcancel")
        self.verticalLayout.addWidget(self.okcancel)
        
        # Set the window title and labels' text
        self.retranslateLoanApp(Loan)
        
        # Connect signals to slots
        self.okcancel.accepted.connect(self.accept)
        self.okcancel.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(Loan)

    def retranslateLoanApp(self, Loan):
        # Set the window title and labels' text
        _translate = QtCore.QCoreApplication.translate
        Loan.setWindowTitle(_translate("Loan", "Dialog"))
        self.welcome_loan.setText(_translate("Loan", "Welcome to Loan Account:"))
        self.ask_loan.setText(_translate("Loan", "What will be your starting Loan?"))
        self.loan_amount.setPlaceholderText(_translate("Loan", "Enter here"))

    def accept(self):
        pass

    def reject(self):
        pass
    def slider_change(self):
        months = self.months_slider.value()
        year = months//12
        months = months%12
        self.months_loan.setText(f"{year} Year(s) and {months} Month(s)")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    # Create the main window
    Loan = QtWidgets.QDialog()
    
    # Create an instance of the Ui_Loan class
    ui = LoanApp()
    ui.setupLoanApp(Loan)
    
    # Show the main window
    Loan.show()
    
    # Start the application event loop
    sys.exit(app.exec_())
