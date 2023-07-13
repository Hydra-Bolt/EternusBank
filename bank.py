from Customer import Customer
import DesignClass
import contextlib
import time
import sys
import random
from datetime import datetime, timedelta, date
import importlib
from PyQt5 import QtCore, QtGui, QtWidgets

importlib.reload(DesignClass)
import pyperclip


class Bank(DesignClass.MasterGUI):
    """Bank class represents the main banking application."""

    def __init__(self, MainWindow: QtWidgets.QMainWindow) -> None:
        """Initialize the Bank class."""
        DesignClass.MasterGUI.__init__(self, MainWindow)
        self.setupDB()
        self.MainWindow.setWindowIcon(QtGui.QIcon("./icons/logo_title.png"))
        self.count = 0

    def generate_credit_card_number(self):
        """Generate a random credit card number."""
        # Generate the first 6 digits (Issuer Identification Number)
        iin = random.choice(["4", "5", "37", "6"]) + "".join(
            random.choice("0123456789") for _ in range(5)
        )

        # Generate the remaining digits (Account Number)
        account_number = "".join(random.choice("0123456789") for _ in range(9))

        return iin + account_number

    def generate_expiry_date(self):
        """Generate a random expiry date for a credit card."""
        # Set the current date
        current_date = datetime.now()

        # Calculate the maximum expiry duration (e.g., 5 years from the current date)
        max_expiry_duration = timedelta(days=365 * 5)

        # Calculate the maximum expiry date
        max_expiry_date = current_date + max_expiry_duration

        return [
            max_expiry_date.strftime("%m/%Y"),
            max_expiry_date.strftime("%B"),
            max_expiry_date.strftime("%Y"),
        ]

    def createAccount(self):    # sourcery skip: extract-method, low-code-quality
        """Create a new bank account for a customer."""
        # List of data fields to be filled
        filling_data = ["Full Name", "CNIC"]

        # List of data entered by the user
        list_of_data = [self.fullname.text(), self.cnic.text()]

        # Generate a random account number
        account_number = (
            "ETR-"
            + "".join([str(random.randint(0, 9)) for _ in range(6)])
            + "-"
            + "".join([str(random.randint(0, 9)) for _ in range(6)])
        )

        print(account_number)

        # List of account information fields
        accounts = ["Phone Number", "Account Number", "Account Type", "Password"]

        # List of account data entered by the user
        accounts_data = [
            self.phone_number.text(),
            account_number,
            self.accountype.currentText(),
            self.password_create.text(),
        ]

        # Create a dictionary with the filling data and corresponding user-entered data
        self.output = {
            filling_data[i]: list_of_data[i] for i in range(len(list_of_data))
        }

        # Check if any of the required information fields are empty
        self.infolist = [i == "" for i in list_of_data]
        accountlist = [i == "" for i in accounts_data]

        # Display an error message if any required field is empty
        if any(self.infolist) or any(accountlist):
            try:
                # print(f"{filling_data[self.infolist.index(True)]} isn't filled")
                QtWidgets.QMessageBox.information(
                    self.MainWindow,
                    "Account Login",
                    f"{filling_data[self.infolist.index(True)]} isn't filled",
                )
            except Exception:
                # print(f"{accounts[accountlist.index(True)]} isn't filled")
                QtWidgets.QMessageBox.information(
                    self.MainWindow,
                    "Account Login",
                    f"{accounts[accountlist.index(True)]} isn't filled",
                )
            return
        else:
            # Create dictionaries for user information and account information
            if len(list_of_data[1]) < 13:
                QtWidgets.QMessageBox.information(
                    self.MainWindow,
                    "Account Signup",
                    "CNIC must be 13 digit long, recheck and re-enter.",
                )
                self.cnic.setText("")
                return

            self.info = {
                filling_data[i]: list_of_data[i] for i in range(len(list_of_data))
            }
            self.account = {
                accounts[i]: accounts_data[i] for i in range(len(accounts_data))
            }
            if self.account["Account Type"] != "Loan Account":
                self.account["Balance"] = 0
                self.account["Card Number"] = self.generate_credit_card_number()
                self.account["Expiry Date"] = self.generate_expiry_date()
                self.account["Transactions"] = []
                if self.account["Account Type"] == "Checking Account":
                    self.account["Overdraft"] = 500
                else:
                    print("savings")
                    self.account["Interest Rate"] = 0.005
                    self.account["Interest Add Date"] = (
                        date.today() + timedelta(days=1)
                    ).strftime("%d/%m/%y")
            else:
                self.output = [self.output]
                self.MainWindow.close()
                self.loan_application = QtWidgets.QDialog()
                self.setupLoanApp(self.loan_application)
                self.loan_application.show()
                print("ran")
            # Check if the user already exists in the database

            if self.account["Account Type"] == "Loan Account":
                return
            if result := list(
                self.userAccountInfo.find({"CNIC": self.info["CNIC"]})
            ):
                QtWidgets.QMessageBox.information(
                    self.MainWindow,
                    "Account Signup",
                    "CNIC found making another account.",
                )
                if (
                    self.account
                    in self.userAccountInfo.find({"CNIC": self.info["CNIC"]})[0][
                        "Accounts"
                    ]
                ):
                    QtWidgets.QMessageBox.information(
                        self.MainWindow,
                        "Account Signup",
                        "Account already exists. Kindly SignUp by exiting the application",
                    )
                    return
                self.userAccountInfo.find({"CNIC": self.info["CNIC"]})[0][
                    "Accounts"
                ].append(self.account)

                self.userAccountInfo.updateDB()
            else:
                print("here")
                self.info |= {"Accounts": [self.account]}
                self.userAccountInfo.insert(self.info)
            self.output = [self.output]
            print(self.output)

            self.openHomeWindow()

    def checkCredentials(self):
        """Check the login credentials entered by the user."""
        filling_data = ["CNIC", "Phone Number", "Password"]
        list_of_data = [
            self.cnic_line_edit.text(),
            self.phone_number_login.text(),
            self.password_login_edit.text(),
        ]

        # Check if any of the fields are empty
        self.infolist = [i == "" for i in list_of_data]
        if any(self.infolist):
            # print(f"{filling_data[self.infolist.index(True)]} isn't filled")
            QtWidgets.QMessageBox.information(
                    self.MainWindow,
                    "Account Login",
                    f"{filling_data[self.infolist.index(True)]} isn't filled",
                )
        else:
            if len(list_of_data[0]) < 13:
                QtWidgets.QMessageBox.information(
                    self.MainWindow,
                    "Account Login",
                    "CNIC must be 13 digit long, recheck and re-enter.",
                )
                self.cnic_line_edit.setText("")
                return
            # Create a dictionary with the filled data
            self.info = {
                filling_data[i]: list_of_data[i] for i in range(len(list_of_data))
            }

            # Search for the account using CNIC
            self.output = self.userAccountInfo.find({"CNIC": self.info["CNIC"]})

            if self.output == []:
                QtWidgets.QMessageBox.warning(
                    self.MainWindow,
                    "Account Login",
                    "No Account found with the provided CNIC.",
                )
            else:
                accounts = self.output[0]["Accounts"]
                for account in accounts:
                    if account["Phone Number"] == self.info["Phone Number"]:
                        break
                else:
                    QtWidgets.QMessageBox.warning(
                        self.MainWindow, "Account Login", "Incorrect Phone Number."
                    )
                    return

                # Check if the entered password matches the account's password
                if account["Password"] != self.info["Password"]:
                    QtWidgets.QMessageBox.warning(
                        self.MainWindow,
                        "Account Login",
                        "Incorrect Password for the account.",
                    )
                elif account["Account Type"] == "Loan Account":
                    # Open the loan window if it's a loan account
                    self.account = account
                    self.openLoanWindow()
                else:
                    # Open the home window for other types of accounts
                    self.account = account
                    self.openHomeWindow()

    def openHomeWindow(self):
        """Open the home window after successful login."""
        super().openHomeWindow()
        self.reveal_bool = True
        hide = "\N{BLACK CIRCLE}"
        # Set the name labels to display the user's full name
        self.name_top.setText(f'Welcome, {self.output[0]["Full Name"]}')
        self.name_card.setText(f'{hide * len(self.output[0]["Full Name"])}')
        self.name_2.setText(f'{hide * len(self.output[0]["Full Name"])}')

        # Set the expiry date labels to display the account's expiry date
        self.expiry_date.setText(hide * len(self.account["Expiry Date"][0]))
        self.expiry.setText(hide * len(self.account["Expiry Date"][0]))
        self.month.setText(hide * len(self.account["Expiry Date"][1]))
        self.year.setText(hide * len(self.account["Expiry Date"][2]))

        # Set the card number labels to display the account's card number
        self.number_2.setText(hide * len(self.account["Card Number"]))
        self.acc_number.setText(hide * len(self.account["Card Number"]))
        self.number.setText(hide * len(self.account["Card Number"]))

        # Check the account type and set the appropriate overdraft or interest rate labels
        if self.account["Account Type"] == "Checking Account":
            self.overdraft.setText(f"+${int(self.account['Overdraft'])}")
        else:
            self.addInterest()
            self.overdraft.setText(
                f"+{int(self.account['Interest Rate'] * self.account['Balance'])}"
            )
        # Set the balance labels to display the account's balance
        self.balance_amount.setText(f"${round(self.account['Balance'], 2)}")
        self.money_label.setText(f"${round(self.account['Balance'], 2)}")

        # Populate the list of accounts for the transfer
        width = self.listofaccounts.geometry().width()
        width/=2
        self.listofaccounts.addItem(
            f"{'Card Number'.ljust(int(width))}{'CNIC'.rjust(int(width))}"
        )
        for i in self.userAccountInfo.data_records:
            for account in i["Accounts"]:
                if account!=self.account:
                    card_numer = account["Card Number"]
                    cnic = i["CNIC"]
                    self.listofaccounts.addItem(
                        f"{card_numer.ljust(int(width))}{cnic.rjust(int(width))}"
                    )

        # calculates the average income and the average expense and initiates the customer class
        self.averageCalculate()
        self.customerInit()
        self.setTransactions()

    def setupDB(self):
        """Sets up Database Instance with refrence to the local files"""
        from database import Hakoniwa

        self.userAccountInfo = Hakoniwa("DB.json")
        print(self.userAccountInfo)

    def customerInit(self):
        """Initializes the customer class"""
        self.current_customer = Customer(
            self.account,
            [self.balance_amount, self.money_label],
            self.overdraft,
            self.deposit_entry,
            self.withdraw_label,
            self.overdraft,
        )
        print(self.current_customer)

    def deposit_money(self):
        """Deposits the money entered in the feild of deposit entry"""
        self.current_customer.deposit()
        print(self.current_customer.current_account["Balance"])
        self.saveToDB()
        self.averageCalculate()
        self.setTransactions()
        # Info Box after Deposit
        QtWidgets.QMessageBox.information(
            self.MainWindow,
            "Deposit",
            "The amount has been deposited successfully.\nPlease do not deposit again.",
        )

    def withdraw_money(self):
        """Withdraws the money entered in the field of withdraw entry"""
        if not self.validateWithdrawal():
            QtWidgets.QMessageBox.information(
                self.MainWindow,
                "Withdraw for Savings",
                "Bank Eternus follows the policy of fixed withdrawal.\nIt is requested you withdraw after a day.",
            )
            return
        init = self.account["Balance"]
        self.current_customer.withdraw()
        fin = self.account["Balance"]
        print(self.account)
        print(self.current_customer.current_account["Balance"])
        # saves to DB
        self.saveToDB()
        self.averageCalculate()
        self.setTransactions()
        QtWidgets.QMessageBox.information(
            self.MainWindow,
            "Withdraw",
            "The amount has been withdrawn successfully."
            if init != fin
            else "The withdrawl was unsuccessful. Credit Limit Reached.",
        )

    def saveToDB(self):
        """Saves the changes made to DB"""
        self.userAccountInfo.updateDB()

    def transfer_funds(self):
        """Transfers the funds from one to another"""
        # gets the current selected option
        transfer_to: str = self.listofaccounts.currentText()
        found_account_name = transfer_to[: transfer_to.find(" ")]
        if found_account_name == "Card":
            QtWidgets.QMessageBox.information(
            self.MainWindow,
            "Transfer",
            "Select a Valid account. You have selected the Header.")
            return
        found_user = self.userAccountInfo.find(
            {"CNIC": transfer_to[(transfer_to.rfind(" ")) + 1 :]}
        )
        print(found_user, found_account_name)
        index = self.userAccountInfo.data_records.index(found_user[0])
        accounts = self.userAccountInfo.data_records[index]["Accounts"]
        for account in accounts:
            if account["Card Number"] == found_account_name:
                break
        else:
            print("Account Not Found")
        found_account = accounts.index(account)
        try:
            transfer_ammount = int(self.transfer_amount.text())
            self.transfer_amount.setText("")
        except Exception:
            print("NAN")
            return
        if self.current_customer.current_account["Balance"] > transfer_ammount:
            QtWidgets.QMessageBox.information(
                self.MainWindow,
                "Transfer Of Funds",
                "Transfer Successfull.\n Transferring Funds now....",
            )
            self.userAccountInfo.data_records[index]["Accounts"][found_account][
                "Balance"
            ] += transfer_ammount
            self.userAccountInfo.data_records[index]["Accounts"][found_account][
                "Transactions"
            ].append(["Deposit", date.today().strftime("%d/%m/%Y"), transfer_ammount])
            self.withdraw_label.setText(str(transfer_ammount))
            self.current_customer.withdraw()
            self.saveToDB()
            return
        QtWidgets.QMessageBox.information(
                self.MainWindow,
                "Transfer Of Funds",
                "You don't have Enough funds to Transfer.",
            )

    def averageCalculate(self):
        withdraw_list = []  # List to store withdrawal amounts
        deposit_list = []  # List to store deposit amounts

        # Printing the account details for debugging purposes

        # Iterating through each transaction in the account's "Transactions" list
        for i in self.account["Transactions"]:
            if i[0] == "Withdraw":
                # Adding withdrawal amount to the list
                withdraw_list.append(int(i[(2)]))
            else:
                # Adding deposit amount to the list
                deposit_list.append(int(i[2]))

        # Checking if there are no withdrawals or deposits in the account
        if not len(withdraw_list) or not len(deposit_list):
            self.income.setText("$0")  # Setting average income label to $0
            self.expense.setText("$0")  # Setting average expense label to $0
            return

        # Calculating and setting the average income label
        self.income.setText(
            f"Average Income: ${round(sum(deposit_list) / len(deposit_list))}"
        )

        # Calculating and setting the average expense label
        self.expense.setText(
            f"Average Expense: ${round(sum(withdraw_list) / len(withdraw_list))}"
        )

    def validateWithdrawal(self):
        if self.account["Account Type"] == "Checking Account":
            return True

        for transaction in self.account["Transactions"]:
            if transaction[0] == "Withdraw":
                break
        else:
            return True

        current_date = datetime.now().date()  # Getting the current date
        # Parsing the date from transaction details
        target_date = datetime.strptime(transaction[1], "%d/%m/%Y").date()
        # Calculating the difference in days
        days_difference = (current_date - target_date).days

        return days_difference >= 1

    def copy_details(self):
        pyperclip.copy(
            f'{self.output[0]["Full Name"]}\n{self.account["Card Number"]}\n{self.account["Expiry Date"][0]}'
        )

    def name_copy(self):
        pyperclip.copy(self.output[0]["Full Name"])

    def number_copy(self):
        pyperclip.copy(self.account["Card Number"])

    def month_copy(self):
        pyperclip.copy(self.account["Expiry Date"][1])

    def year_copy(self):
        pyperclip.copy(self.account["Expiry Date"][2])

    def reveal_details(self):  # sourcery skip: extract-method
        # Create a message box to prompt the user
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Confirmation")
        msg_box.setText(
            (
                "Are you sure you want to reveal the details?"
                if self.reveal_bool
                else "Are you sure you want to hide the details?"
            )
        )
        msg_box.setIcon(QtWidgets.QMessageBox.Question)
        msg_box.setStandardButtons(
            QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel
        )
        msg_box.setDefaultButton(QtWidgets.QMessageBox.Cancel)

        # Execute the message box and get the user's choice
        choice = msg_box.exec()

        if choice == QtWidgets.QMessageBox.Ok:
            # checks if the data has been revealed or not
            if self.reveal_bool:
                # sets the data from the database
                self.name_card.setText(self.output[0]["Full Name"])
                self.name_2.setText(self.output[0]["Full Name"])

                # Set the expiry date labels to display the account's expiry date
                self.expiry_date.setText(self.account["Expiry Date"][0])
                self.expiry.setText(self.account["Expiry Date"][0])
                self.month.setText(self.account["Expiry Date"][1])
                self.year.setText(self.account["Expiry Date"][2])

                # Set the card number labels to display the account's card number
                self.number_2.setText(self.account["Card Number"])
                self.acc_number.setText(self.account["Card Number"])
                self.number.setText(self.account["Card Number"])
                self.reveal_bool = False
            else:
                hide = "\N{BLACK CIRCLE}"
                # sets to the blurred data
                self.name_card.setText(f'{hide * len(self.output[0]["Full Name"])}')
                self.name_2.setText(f'{hide * len(self.output[0]["Full Name"])}')

                # Set the expiry date labels to display the account's expiry date
                self.expiry_date.setText(hide * len(self.account["Expiry Date"][0]))
                self.expiry.setText(hide * len(self.account["Expiry Date"][0]))
                self.month.setText(hide * len(self.account["Expiry Date"][1]))
                self.year.setText(hide * len(self.account["Expiry Date"][2]))

                # Set the card number labels to display the account's card number
                self.number_2.setText(hide * len(self.account["Card Number"]))
                self.acc_number.setText(hide * len(self.account["Card Number"]))
                self.number.setText(hide * len(self.account["Card Number"]))

    def setTransactions(self):
        print("called")
        style_deposit = "*{color:green;}"
        style_withdraw = "*{color:red;}"

        if not self.count:
            # Create a QLabel for displaying "Recent Transactions"
            self.recent_transactions = QtWidgets.QLabel(self.transactions)
            self.recent_transactions.setMaximumSize(QtCore.QSize(16777215, 40))
            self.recent_transactions.setStyleSheet(
                'color:green;font: 24pt "Modern No. 20";'
            )
            self.recent_transactions.setObjectName("recent_transactions")
            self.recent_transactions.setText("Recent Transactions")
            self.verticalLayout_21.addWidget(self.recent_transactions)

            self.count += 1

            # Add transaction QLabel widgets to the layout
            self.verticalLayout_21.addWidget(self.transaction_1)
            self.verticalLayout_21.addWidget(self.transaction_2)
            self.verticalLayout_21.addWidget(self.transaction_3)

        # Show transaction QLabel widgets
        self.transaction_3.show()
        self.transaction_2.show()
        self.transaction_1.show()

        transactions:list = (self.account["Transactions"])[:-4:-1]
        # transactions.reverse()
        self.no_transactions.hide()

        if len(transactions) > 2:
            # Display transaction information for the latest three transactions
            self.withdrawn_1.setText(transactions[-1][0])
            self.date_1.setText(transactions[-1][1])
            self.amount_1.setText(str(transactions[-1][2]))

            self.withdraw_2.setText(transactions[-2][0])
            self.date_2.setText(transactions[-2][1])
            self.amount_2.setText(str(transactions[-2][2]))

            self.withdraw_3.setText(transactions[-3][0])
            self.date_3.setText(transactions[-3][1])
            self.amount_3.setText(str(transactions[-3][2]))
        elif len(transactions) == 2:
            # Display transaction information for the latest two transactions
            self.withdrawn_1.setText(transactions[-1][0])
            self.date_1.setText(transactions[-1][1])
            self.amount_1.setText(str(transactions[-1][2]))

            self.withdraw_2.setText(transactions[-2][0])
            self.date_2.setText(transactions[-2][1])
            self.amount_2.setText(str(transactions[-2][2]))

            # Hide the third transaction QLabel widget
            self.transaction_3.hide()
        elif len(transactions) == 1:
            # Display transaction information for the latest transaction
            self.withdrawn_1.setText(transactions[-1][0])
            self.date_1.setText(transactions[-1][1])
            self.amount_1.setText(str(transactions[0][2]))

            # Hide the second and third transaction QLabel widgets
            self.transaction_3.hide()
            self.transaction_2.hide()
        else:
            # Hide all transaction QLabel widgets and display "No transactions" message
            self.transaction_3.hide()
            self.transaction_2.hide()
            self.transaction_1.hide()
            self.no_transactions.show()
            self.verticalLayout_21.addWidget(self.no_transactions)
            return

        for i, j in enumerate(
            [self.transaction_3, self.transaction_2, self.transaction_1]
        ):
            current = j.styleSheet()
            with contextlib.suppress(IndexError):
                print(transactions)
                if (
                    transactions[i][0] == "Withdraw"
                ):  # Check transaction type at index 0
                    print(transactions[i][0])
                    current += style_withdraw
                    j.setStyleSheet(current)
                else:
                    print(transactions[i][0])
                    current += style_deposit
                    j.setStyleSheet(current)

    # Loan Methods

    def loan_customer_init(self):
        # Initialize the loan customer with relevant information
        self.loan_customer = Customer(
            current_account=self.account,
            balance_labels=[self.total_repay, self.month_amount],
            withdraw_edit=self.repay_edit,
        )

    def repay_money(self):
        """Withdraws money from the loan customer's account and updates the loan details."""
        amount = self.loan_customer.withdraw()
        if amount is None:
            return
        current_due = self.calculate_current_due()

        try:
            if self.account["Due Dates"][list(self.account["Due Dates"].keys())[-1]] == 0:
                # No more dues remaining, all payments made
                QtWidgets.QMessageBox.information(
                    self.MainWindow, "Loan Repayment", "No more dues remaining. Loan fully repaid. Deleting and Exiting the account. Goodbye."
                )
                self.MainWindow.close()
                return

            if amount <= self.account["Due Dates"][current_due]:
                # Subtract the amount from the current due date
                self.account["Due Dates"][current_due] -= amount
            else:
                # Calculate the remaining amount after paying the current due date
                remaining_amount = amount - self.account["Due Dates"][current_due]

                # Update the current due date to the next one
                next_due_dates = list(self.account["Due Dates"].keys())
                current_due_index = next_due_dates.index(current_due)
                self.account["Due Dates"][current_due] = 0

                # Pay the remaining amount for the next due dates
                for i in range(current_due_index + 1, len(next_due_dates)):
                    due_date = next_due_dates[i]
                    if remaining_amount >= self.account["Due Dates"][due_date]:
                        remaining_amount -= self.account["Due Dates"][due_date]
                        self.account["Due Dates"][due_date] = 0
                    else:
                        self.account["Due Dates"][due_date] -= remaining_amount
                        remaining_amount = 0
                        break

            self.saveToDB()
            QtWidgets.QMessageBox.information(
                self.MainWindow, "Loan Repayment", "Payment successful."
            )
        except KeyError:
            # The current due date doesn't exist
            QtWidgets.QMessageBox.warning(
                self.MainWindow,
                "Loan Repayment",
                "There is no due date available for repayment.",
            )

    def calculate_duedates(self, money):
        # Calculate the due dates for the loan repayments based on the loan amount
        return {
            (
                datetime.strptime(self.account["Date Made"], "%d/%m/%y")
                + timedelta(days=30 * i + 1)
            ).strftime("%d/%m/%y"): float(money / (self.months_slider.value()))
            for i in range(self.months_slider.value())
        }

    def calculate_current_due(self):
        # Calculate the current due date for the loan repayment
        for date_ in self.account["Due Dates"]:
            if datetime.strptime(date_, "%d/%m/%y").date() > date.today():
                return date_

    def passedDates(self):
        # Get the passed due dates for the loan repayments
        passed_dates, due_dates = {}, self.account["Due Dates"]
        for date_ in due_dates:
            if date.today() < datetime.strptime(date_, "%d/%m/%y").date():
                print(date_)
                return passed_dates
            else:
                passed_dates[date_] = due_dates[date_]
        return passed_dates

    def accept(self):
        """If user accepts the Loan"""
        # Update account information with the accepted loan details
        try:
            
            self.account["Net Pay"] = int(self.loan_amount.text()) + int(
                int(self.loan_amount.text()) * 0.26
            )
        except:
            QtWidgets.QMessageBox.warning(
                self.MainWindow,
                "Loan Account",
                "Enter the Amount of Loan.",
            )
            return
        self.account["Card Number"] = self.generate_credit_card_number()
        self.account["Date Made"] = date.today().strftime("%d/%m/%y")
        self.account["Due Dates"] = self.calculate_duedates(self.account["Net Pay"])
        print(self.calculate_current_due())
        print("RAN")
        self.loan_application.close()
        # Check if the user has an existing account or not
        if list(self.userAccountInfo.find({"CNIC": self.info["CNIC"]})) != []:
            print("found")
            # Add the account to the existing user's accounts
            self.userAccountInfo.find({"CNIC": self.info["CNIC"]})[0][
                "Accounts"
            ].append(self.account)
            self.userAccountInfo.updateDB()

        else:
            print("here")
            # Create a new user account with the loan account
            self.info |= {"Accounts": [self.account]}
            self.userAccountInfo.insert(self.info)
        self.openLoanWindow()

    def openLoanWindow(self):
        """Opens loan window and sets up the window"""
        # Set up the loan window
        self.setupUi_loan(self.MainWindow)

        self.MainWindow.show()
        self.loan_customer_init()
        passed = self.passedDates()
        if passed != {}:
            self.account["Due Dates"] = self.calculate_duedates(
                self.account["Net Pay"] + sum(passed.values())
            )

        self.current_due = self.calculate_current_due()
        self.month_amount.setText(f"${self.account['Due Dates'][self.current_due]}")
        self.ammountToBePaid.setText(f"Due Date: {self.current_due}")
        self.total_repay.setText(f'${self.account["Net Pay"]}')
        self.name_loan.setText(f"{self.output[0]['Full Name']}")

    def reject(self):
        """Closes the window if user rejects."""
        # Close the loan application window and the main window
        self.loan_application.close()
        self.MainWindow.close()
        self.__init__(self.MainWindow)

    # Savings Account

    def addInterest(self):
        # Add interest to the savings account balance
        current_interest_date = datetime.strptime(
            self.account["Interest Add Date"], "%d/%m/%y"
        ).date()
        current_date = date.today()
        print(current_interest_date, current_date)
        if current_date >= current_interest_date:
            print("hehe")
            self.account["Balance"] += (
                self.account["Balance"] * self.account["Interest Rate"]
            )
            self.account["Interest Add Date"] = (
                current_interest_date + timedelta(days=1)
            ).strftime("%d/%m/%y")
            print(self.account["Balance"])
            self.addInterest()
        self.saveToDB()

    def logout(self):
        confirm = QtWidgets.QMessageBox()
        confirm.setWindowTitle("Confirmation")
        confirm.setText(("Are you sure you want to logout?"))
        confirm.setIcon(QtWidgets.QMessageBox.Question)
        confirm.setStandardButtons(
            QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel
        )
        confirm.setDefaultButton(QtWidgets.QMessageBox.Cancel)

        # Execute the message box and get the user's choice
        choice = confirm.exec()
        if choice == QtWidgets.QMessageBox.Ok:
            self.MainWindow.close()
            self.__init__(self.MainWindow)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

bank = Bank(MainWindow=MainWindow)
sys.exit(app.exec_())
