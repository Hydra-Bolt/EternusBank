
from adminLogin import AdminLogin
from adminWindow import AdminWindow
from report import Report
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys


class Admin(AdminLogin, AdminWindow):
    def __init__(self, Window: QtWidgets.QMainWindow) -> None:
        self.setupDB()
        self.Window = Window
        self.setup_ALoginUi(self.Window)
        self.Window.show()

    def authenticateLogin(self):
        admins = {"Muneeb": "muneeb123123", "Tehreem": "tehreemkhan6677","a":"a"}
        if self.user_edit.text() in admins:
            if admins[self.user_edit.text()] == self.password_edit.text():
                self.openWindow()
            else:
                QtWidgets.QMessageBox.warning(
                    self.Window,
                    "Admin Login",
                    "Incorrect Password for the admin.",
                )
            return
        QtWidgets.QMessageBox.warning(
            self.Window,
            "Account Login",
            "Admin doesn't exist. Username incorrect",
        )

    def generateReport(self):
        """Generates Report for the User"""

        # Create a new dialog window
        self.dialog = QtWidgets.QDialog()
        self.dialog.setWindowTitle("Delete Record")
        self.dialog.setStyleSheet(
            'font: 16pt "Modern No. 20";border-radius:5px;border:1px solid black;padding:6px'
        )
        self.dialog.setMinimumSize(600, 400)
        self.dialog.resize(600, 400)

        # Create combo box, label, and buttons
        combo_box = QtWidgets.QComboBox(self.dialog)
        label = QtWidgets.QLabel(
            "Select which account you would like the report of:", self.dialog
        )
        ok_button = QtWidgets.QPushButton("OK", self.dialog)
        cancel_button = QtWidgets.QPushButton("Cancel", self.dialog)

        # Populate combo box with numbers
        records = [str(i) for i in range(1, self.details_table.rowCount() + 1)]
        combo_box.addItems(records)

        # Layout configuration
        layout = QtWidgets.QVBoxLayout(self.dialog)
        layout.addWidget(label)
        layout.addWidget(combo_box)
        layout.addStretch(1)
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

        # Connect the button signals to their respective functions
        ok_button.clicked.connect(self.dialog.accept)
        cancel_button.clicked.connect(self.dialog.reject)

        # Check if the dialog was accepted or rejected
        if self.dialog.exec_() != QtWidgets.QDialog.Accepted:
            return

        # Get the selected record from the combo box and retrieve associated details
        record = int(combo_box.currentText()) - 1
        cnic = self.details_table.item(record, 1).text()
        acc_num = self.details_table.item(record, 2).text()

        # Retrieve account information from the database
        out = (self.userAccountInfo.find({"CNIC": cnic}))[0]
        accounts: list = out["Accounts"]

        # Find the selected account based on the account number
        for account in accounts:
            if account["Account Number"] == acc_num:
                break

        # Create a new report instance
        report = Report()
        report.add_page()
        report.set_auto_page_break(auto=True, margin=15)
        report.set_font("Arial", "", 10)

        # Add chapter title and body for account information
        report.chapter_title("Account Information")
        report.chapter_body(
            [
                {"Full Name": out["Full Name"]},
                {"CNIC": out["CNIC"]},
                {"Phone Number": account["Phone Number"]},
                {"Account Number": account["Account Number"]},
                {"Account Type": account["Account Type"]},
                {"Balance": account["Balance"]},
                {"Card Number": "3759577752541257"},
                {"Expiry Date": account["Expiry Date"][0]},
            ]
        )

        # Add chapter title and body for transactions
        report.chapter_title("Transactions")
        report.chapter_body([{"Transactions": account["Transactions"]}])

        # Add a new page and chapter title for recent transaction graph
        report.add_page()
        report.chapter_title("Recent Transaction Graph")

        # Check if there are transactions to plot
        if account["Transactions"] != []:
            self.generate_graph(account)
            report.image(f"./customer_graphs/{account['Account Number']}.png", w=200)
        else:
            report.chapter_body({"Transactions": "No Transactions to plot"})

        # Generate the PDF report file
        report.output(f"./customer_reports/{out['Full Name']}_{out['CNIC']}.pdf")
        os.system(f"./customer_reports/{out['Full Name']}_{out['CNIC']}.pdf")
    def generate_graph(self, account):
        import pandas as pd
        import datetime
        import matplotlib.pyplot as plt

        # Initializing variables
        transaction_history = []
        transaction_dates = {}

        # Iterate through each transaction in the account's transaction list
        for transaction in account["Transactions"]:
            if transaction[1] not in transaction_dates:
                transaction_dates[transaction[1]] = []
            if transaction[0] == "Withdraw":
                transaction_dates[transaction[1]].append(-int(transaction[2]))
            else:
                transaction_dates[transaction[1]].append(int(transaction[2]))

        # Extract unique transaction dates and calculate the total amount for each date
        transaction_history = list(transaction_dates.keys())
        transaction_money = [sum(date) for date in transaction_dates.values()]

        # Create a pandas Series and DataFrame for the transaction history
        transaction_history = pd.Series(transaction_history)
        transaction_history = pd.DataFrame(
            transaction_history, columns=["Transaction Dates"]
        )
        transaction_history["Amount"] = transaction_money

        # Limit the transaction history to the last 7 entries if there are more than 7
        if len(transaction_history["Transaction Dates"]) >= 7:
            transaction_history["Transaction Dates"] = transaction_history[
                "Transaction Dates"
            ][:7]

        # Extend the transaction history with previous dates if there are less than 7 entries
        elif len(transaction_history["Transaction Dates"]) < 7:
            rem_dates = 7 - len(transaction_history["Transaction Dates"])
            new_list = []
            for i in range(rem_dates):
                new_date = (
                    datetime.datetime.strptime(
                        transaction_history["Transaction Dates"][0], "%d/%m/%Y"
                    ).date()
                    - datetime.timedelta(days=i + 1)
                ).strftime("%d/%m/%Y")
                new_list.append(new_date)
            new_list.reverse()
            new_list.extend(transaction_history["Transaction Dates"])

        transaction_history = pd.DataFrame(new_list, columns=["Transaction Dates"])

        transaction_money.reverse()
        transaction_money += [0 for _ in range(rem_dates)]
        transaction_money.reverse()

        transaction_history["Amount"] = transaction_money

        font = {"fontname": "Arial", "fontsize": 14}
        fig = plt.figure(figsize=(12, 4))
        ax = plt.axes(facecolor="white")
        ax.spines["top"].set_color("white")
        ax.spines["right"].set_color("white")

        # Set font properties for x and y ticks
        plt.xticks(**font)
        plt.yticks(**font)

        # sets the buffer for limits
        # Set the y-axis limits based on the minimum and maximum transaction amounts
        plt.ylim(min(transaction_money), max(transaction_money))

        # Plot a bar graph of the transaction dates and amounts
        plt.bar(
            transaction_history["Transaction Dates"],
            transaction_history["Amount"],
            color=["green" if amount >= 0 else "red" for amount in transaction_history["Amount"]],
        )


        # Save the graph as a PNG file
        plt.savefig(f"./customer_graphs/{account['Account Number']}.png")

    def deleteRecords(self):
        """Deletes a record at a certain index"""
        self.dialog = QtWidgets.QDialog()
        self.dialog.setWindowTitle("Delete Record")
        self.dialog.setStyleSheet(
            'font: 16pt "Modern No. 20";border-radius:5px;border:1px solid black;padding:6px'
        )
        self.dialog.setMinimumSize(600, 400)
        self.dialog.resize(600, 400)
        combo_box = QtWidgets.QComboBox(self.dialog)
        label = QtWidgets.QLabel("Select record to delete:", self.dialog)
        ok_button = QtWidgets.QPushButton("OK", self.dialog)
        cancel_button = QtWidgets.QPushButton("Cancel", self.dialog)

        # Populate combo box with numbers
        records = [str(i) for i in range(1, self.details_table.rowCount() + 1)]
        combo_box.addItems(records)

        # Layout configuration
        layout = QtWidgets.QVBoxLayout(self.dialog)
        layout.addWidget(label)
        layout.addWidget(combo_box)
        layout.addStretch(1)
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

        # Connect the button signals to their respective functions
        ok_button.clicked.connect(self.dialog.accept)
        cancel_button.clicked.connect(self.dialog.reject)

        if self.dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.deleteRecord(combo_box.currentText())

    def deleteRecord(self, record) -> None:
        record = int(record) - 1
        cnic = self.details_table.item(record, 1).text()
        acc_num = self.details_table.item(record, 2).text()

        out = (self.userAccountInfo.find({"CNIC": cnic}))[0]
        accounts: list = out["Accounts"]

        for index, account in enumerate(accounts):
            if account["Account Number"] == acc_num:
                accounts.pop(index)
        self.userAccountInfo.update_insert({"CNIC": cnic}, out)
        self.userAccountInfo.updateDB()
        self.configTable()

    def updateRecords(self, row, column):
        """Updates Records for every changes in tables"""
        item = self.details_table.item(row, column)
        if item is None:
            QtWidgets.QMessageBox.critical(
                self.Window,
                "DataBase Change",
                "Oops, an error occured!",
            )
            return
        changed_value = item.text()
        changed_key = self.fields[column]
        cnic_item = self.details_table.item(row, 1)
        c_number_item = self.details_table.item(row, 4)
        ac_number_item = self.details_table.item(row,2)
        
        if cnic_item is None or c_number_item is None or ac_number_item is None:
            return
        cnic_value = cnic_item.text()
        c_number = c_number_item.text()
        ac_number = ac_number_item.text()
        output = (self.userAccountInfo.find({"CNIC": cnic_value}))[0]
        if changed_key in ["Full Name", "CNIC"]:
            output[changed_key] = changed_value
        else:
            if changed_key == "Account Number":
                for account in output["Accounts"]:
                    if account["Card Number"] == c_number:
                        break
            else:
                for account in output["Accounts"]:
                    if account["Account Number"] == ac_number:
                        break
                
            account[changed_key] = changed_value
        self.userAccountInfo.update_insert({"CNIC": cnic_value}, output)
        self.userAccountInfo.updateDB()

    def openWindow(self):
        """Opens Window for Admin and sets up table"""
        self.Window.close()
        self.setup_AWindowUi(self.Window)
        self.Window.show()
        self.fields = [
            "Full Name",
            "CNIC",
            "Account Number",
            "Account Type",
            "Card Number",
            "Phone Number",
            "Balance",
        ]
        self.details_table.setColumnCount(len(self.fields))
        self.details_table.setHorizontalHeaderLabels(self.fields)
        self.configTable()

    def configTable(self):
        """Configures Table for DataRecords"""
        current_index = 0
        for record in self.userAccountInfo.data_records:
            name = record["Full Name"]
            cnic = record["CNIC"]
            accounts = record["Accounts"]
            for account in accounts:
                
                self.details_table.setRowCount(current_index + 1)
                # self.details_table.setVerticalHeaderItem(current_index, QtWidgets.QTableWidgetItem(current_index))
                try:
                    self.details_table.setItem(
                        current_index, 0, QtWidgets.QTableWidgetItem(name)
                    )
                    self.details_table.setItem(
                        current_index, 1, QtWidgets.QTableWidgetItem(cnic)
                    )
                    self.details_table.setItem(
                        current_index,
                        2,
                        QtWidgets.QTableWidgetItem(account["Account Number"]),
                    )
                    self.details_table.setItem(
                        current_index,
                        3,
                        QtWidgets.QTableWidgetItem(account["Account Type"]),
                    )
                    self.details_table.setItem(
                        current_index, 4, QtWidgets.QTableWidgetItem(account["Card Number"])
                    )
                    self.details_table.setItem(
                        current_index,
                        5,
                        QtWidgets.QTableWidgetItem(account["Phone Number"]),
                    )
                    self.details_table.setItem(
                        current_index,
                        6,
                        QtWidgets.QTableWidgetItem(str(account["Balance"])),
                    )
                except KeyError:
                    # self.details_table.setVerticalHeaderItem(current_index, QtWidgets.QTableWidgetItem(current_index))
                    self.details_table.setItem(
                        current_index, 0, QtWidgets.QTableWidgetItem(name)
                    )
                    self.details_table.setItem(
                        current_index, 1, QtWidgets.QTableWidgetItem(cnic)
                    )
                    self.details_table.setItem(
                        current_index,
                        2,
                        QtWidgets.QTableWidgetItem(account["Account Number"]),
                    )
                    self.details_table.setItem(
                        current_index,
                        3,
                        QtWidgets.QTableWidgetItem(account["Account Type"]),
                    )
                    self.details_table.setItem(
                        current_index, 4, QtWidgets.QTableWidgetItem(account["Card Number"])
                    )
                    self.details_table.setItem(
                        current_index,
                        5,
                        QtWidgets.QTableWidgetItem(account["Phone Number"]),
                    )
                    self.details_table.setItem(
                        current_index,
                        6,
                        QtWidgets.QTableWidgetItem(str(account["Net Pay"])),
                    )
                current_index += 1

    def setupDB(self):
        """Sets up Database Instance with refrence to the local files"""
        from database import Hakoniwa

        self.userAccountInfo = Hakoniwa("DB.json")

    def searchRecord(self):
        search_item = self.search.text()
        for row in range(self.details_table.rowCount()):
            for col in range(self.details_table.columnCount()):
                item = self.details_table.item(row, col)
                if item is None:
                    return
                if search_item.lower() in item.text().lower() and search_item != "":
                    item.setBackground(QtGui.QColor("#D1FFDB"))
                else:
                    item.setBackground(QtGui.QColor("white"))

    def buttonclick(self, button: QtWidgets.QPushButton):
        init_rect = button.geometry()
        new_rect = QtCore.QRect(*[int(x / 1.1) for x in init_rect.getRect()])
        new_rect.translate(
            init_rect.x() - new_rect.x() + int(new_rect.width() // 20),
            init_rect.y() - new_rect.y() + int(new_rect.height() // 20),
        )
        button.setGeometry(new_rect)
        # Create a QTimer object
        self.timer1 = QtCore.QTimer()
        self.timer1.setSingleShot(True)  # Set the timer to fire only once

        def reset_button_geometry():
            # Reset button geometry to original state
            button.setGeometry(init_rect)

        self.timer1.timeout.connect(reset_button_geometry)

        # Start the timer with a timeout of 2000 milliseconds (2 seconds)
        self.timer1.start(100)
        button.setEnabled(False)
        try:
            # Create a QTimer object
            self.timer2 = QtCore.QTimer()

            # Set up the timeout function to enable the button after the specified duration
            self.timer2.timeout.connect(lambda: button.setEnabled(True))

            # Start the timer
            self.timer2.start(5000)
        except RuntimeError:
            pass


app = QtWidgets.QApplication(sys.argv)
Window = QtWidgets.QMainWindow()
ui = Admin(Window)
sys.exit(app.exec_())
