from re import I
from adminLogin import AdminLogin
from adminWindow import AdminWindow
from report import Report
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys


class Admin:
    def __init__(self, Window: QtWidgets.QMainWindow) -> None:
        self.setupDB()
        self.admin_login = AdminLogin()
        self.admin_window = AdminWindow()
        self.Window = Window
        self.admin_login.setup_ALoginUi(self.Window)
        self.admin_login.submit_button.clicked.connect(self.authenticateLogin)
        self.Window.show()

    def authenticateLogin(self):
        admins = {"Muneeb": "muneeb123123", "Tehreem": "tehreemkhan6677"}
        if self.admin_login.user_edit.text() in admins:
            if admins[self.admin_login.user_edit.text()] == self.admin_login.password_edit.text():
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
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Delete Record")
        dialog.setStyleSheet(
            'font: 16pt "Modern No. 20";border-radius:5px;border:1px solid black;padding:6px'
        )
        dialog.setMinimumSize(600, 400)
        dialog.resize(600, 400)

        combo_box = QtWidgets.QComboBox(dialog)
        label = QtWidgets.QLabel(
            "Select which account you would like the report of:", dialog
        )
        ok_button = QtWidgets.QPushButton("OK", dialog)
        cancel_button = QtWidgets.QPushButton("Cancel", dialog)

        records = [str(i) for i in range(1, self.admin_window.details_table.rowCount() + 1)]
        combo_box.addItems(records)

        layout = QtWidgets.QVBoxLayout(dialog)
        layout.addWidget(label)
        layout.addWidget(combo_box)
        layout.addStretch(1)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

        ok_button.clicked.connect(dialog.accept)
        cancel_button.clicked.connect(dialog.reject)

        if dialog.exec_() != QtWidgets.QDialog.Accepted:
            return

        record = int(combo_box.currentText()) - 1
        cnic = self.admin_window.details_table.item(record, 1).text()
        acc_num = self.admin_window.details_table.item(record, 2).text()

        out = (self.userAccountInfo.find({"CNIC": cnic}))[0]
        accounts: list = out["Accounts"]

        for account in accounts:
            if account["Account Number"] == acc_num:
                break

        report = Report()
        report.add_page()
        report.set_auto_page_break(auto=True, margin=15)
        report.set_font("Arial", "", 10)

        report.chapter_title("Account Information")
        try:
            report.chapter_body(
                [
                    {"Full Name": out["Full Name"]},
                    {"CNIC": out["CNIC"]},
                    {"Account Name": account["Account Name"]},
                    {"Account Number": account["Account Number"]},
                    {"Account Type": account["Account Type"]},
                    {"Balance": account["Balance"]},
                    {"Card Number": "3759577752541257"},
                    {"Expiry Date": account["Expiry Date"][0]},
                ]
            )
        except:
            report.chapter_body(
                [
                    {"Full Name": out["Full Name"]},
                    {"CNIC": out["CNIC"]},
                    {"Account Name": account["Account Name"]},
                    {"Account Number": account["Account Number"]},
                    {"Account Type": account["Account Type"]},
                    {"Balance": account["Balance"]},
                    {"Card Number": "3759577752541257"},
                    {"Expiry Date": account["Due Dates"][(list(account["Due Dates"].keys())[-1])]},
                ]
            )
        report.chapter_title("Transactions")
        report.chapter_body([{"Transactions": account["Transactions"]}])

        report.add_page()
        report.chapter_title("Recent Transaction Graph")

        if account["Transactions"] != []:
            self.generate_graph(account)
            report.image(f"./customer_graphs/{account['Account Number']}.png", w=200)
        else:
            report.chapter_body({"Transactions": "No Transactions to plot"})

        report.output(f"./customer_reports/{out['Full Name']}_{out['CNIC']}.pdf")
        os.system(f"./customer_reports/{out['Full Name']}_{out['CNIC']}.pdf")

    def generate_graph(self, account):
        import pandas as pd
        import datetime
        import matplotlib.pyplot as plt

        transaction_history = []
        transaction_dates = {}

        for transaction in account["Transactions"]:
            if transaction[1] not in transaction_dates:
                transaction_dates[transaction[1]] = []
            if transaction[0] == "Withdraw":
                transaction_dates[transaction[1]].append(-int(transaction[2]))
            else:
                transaction_dates[transaction[1]].append(int(transaction[2]))

        transaction_history = list(transaction_dates.keys())
        transaction_money = [sum(date) for date in transaction_dates.values()]

        transaction_history = pd.Series(transaction_history)
        transaction_history = pd.DataFrame(
            transaction_history, columns=["Transaction Dates"]
        )
        transaction_history["Amount"] = transaction_money

        if len(transaction_history["Transaction Dates"]) >= 7:
            transaction_history["Transaction Dates"] = transaction_history["Transaction Dates"][:7]
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
        transaction_money = transaction_money + [0 for i in range(rem_dates)]
        transaction_money.reverse()

        transaction_history["Amount"] = transaction_money

        font = {"fontname": "Arial", "fontsize": 14}
        fig = plt.figure(figsize=(12, 4))
        ax = plt.axes(facecolor="white")
        ax.spines["top"].set_color("white")
        ax.spines["right"].set_color("white")

        plt.xticks(**font)
        plt.yticks(**font)

        buffer = 100
        plt.ylim(min(transaction_money) - buffer, max(transaction_money) + buffer)

        plt.bar(
            transaction_history["Transaction Dates"],
            transaction_history["Amount"],
            color=[
                "green" if amount >= 0 else "red"
                for amount in transaction_history["Amount"]
            ],
        )

        plt.savefig(f"./customer_graphs/{account['Account Number']}.png")

    def deleteRecords(self):
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Delete Record")
        dialog.setStyleSheet(
            'font: 16pt "Modern No. 20";border-radius:5px;border:1px solid black;padding:6px'
        )
        dialog.setMinimumSize(600, 400)
        dialog.resize(600, 400)

        combo_box = QtWidgets.QComboBox(dialog)
        label = QtWidgets.QLabel("Select record to delete:", dialog)
        ok_button = QtWidgets.QPushButton("OK", dialog)
        cancel_button = QtWidgets.QPushButton("Cancel", dialog)

        records = [str(i) for i in range(1, self.admin_window.details_table.rowCount() + 1)]
        combo_box.addItems(records)

        layout = QtWidgets.QVBoxLayout(dialog)
        layout.addWidget(label)
        layout.addWidget(combo_box)
        layout.addStretch(1)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

        ok_button.clicked.connect(dialog.accept)
        cancel_button.clicked.connect(dialog.reject)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.deleteRecord(combo_box.currentText())

    def deleteRecord(self, record) -> None:
        record = int(record) - 1
        cnic = self.admin_window.details_table.item(record, 1).text()
        acc_num = self.admin_window.details_table.item(record, 2).text()

        out = (self.userAccountInfo.find({"CNIC": cnic}))[0]
        accounts: list = out["Accounts"]

        for index, account in enumerate(accounts):
            if account["Account Number"] == acc_num:
                accounts.pop(index)
        self.userAccountInfo.update_insert({"CNIC": cnic}, out)
        self.userAccountInfo.updateDB()
        self.configTable()

    def updateRecords(self, row, column):
        item = self.admin_window.details_table.item(row, column)
        if item is None:
            QtWidgets.QMessageBox.critical(
                self.admin_window,
                "DataBase Change",
                "Oops, an error occurred!",
            )
            return
        changed_value = item.text()
        changed_key = self.fields[column]
        cnic_item = self.admin_window.details_table.item(row, 1)
        if cnic_item is None:
            return
        cnic_value = cnic_item.text()
        output = (self.userAccountInfo.find({"CNIC": cnic_value}))[0]
        if changed_key in ["Full Name", "CNIC"]:
            output[changed_key] = changed_value
        else:
            if changed_key == "Account Number":
                for account in output["Accounts"]:
                    if account["Account Number"] == changed_value:
                        self.account = account
            self.account[changed_key] = changed_value
        self.userAccountInfo.update_insert({"CNIC": cnic_value}, output)
        self.userAccountInfo.updateDB()


    def openWindow(self):
        self.Window.close()
        self.admin_window.setup_AWindowUi(self.Window)
        self.admin_window.delete_records.clicked.connect(self.deleteRecords)
        self.admin_window.generate_report.clicked.connect(self.generateReport)
        self.admin_window.details_table.cellChanged.connect(self.updateRecords)
        self.admin_window.delete_records.clicked.connect(lambda:self.buttonclick(self.admin_window.delete_records))
        self.admin_window.generate_report.clicked.connect(self.generateReport)
        self.admin_window.generate_report.clicked.connect(lambda:self.buttonclick(self.admin_window.generate_report))
        self.admin_window.search.textChanged.connect(self.searchRecord)
        self.admin_window.search.setPlaceholderText("Search...")
        self.admin_window.delete_records.setText("Delete Record")
        self.admin_window.generate_report.setText("Generate Report")
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
        self.admin_window.details_table.setColumnCount(len(self.fields))
        self.admin_window.details_table.setHorizontalHeaderLabels(self.fields)
        self.configTable()

    def configTable(self):
        current_index = 0
        for record in self.userAccountInfo.data_records:
            name = record["Full Name"]
            cnic = record["CNIC"]
            accounts = record["Accounts"]
            for account in accounts:
                self.admin_window.details_table.setRowCount(current_index + 1)
                try:
                    self.admin_window.details_table.setItem(
                        current_index, 0, QtWidgets.QTableWidgetItem(name)
                    )
                    self.admin_window.details_table.setItem(
                        current_index, 1, QtWidgets.QTableWidgetItem(cnic)
                    )
                    self.admin_window.details_table.setItem(
                        current_index,
                        2,
                        QtWidgets.QTableWidgetItem(account["Account Number"]),
                    )
                    self.admin_window.details_table.setItem(
                        current_index,
                        3,
                        QtWidgets.QTableWidgetItem(account["Account Type"]),
                    )
                    self.admin_window.details_table.setItem(
                        current_index, 4, QtWidgets.QTableWidgetItem(account["Card Number"])
                    )
                    self.admin_window.details_table.setItem(
                        current_index,
                        5,
                        QtWidgets.QTableWidgetItem(account["Account Name"]),
                    )
                    self.admin_window.details_table.setItem(
                        current_index,
                        6,
                        QtWidgets.QTableWidgetItem(str(account["Balance"])),
                    )
                except KeyError:
                    self.admin_window.details_table.setItem(
                        current_index, 0, QtWidgets.QTableWidgetItem(name)
                    )
                    self.admin_window.details_table.setItem(
                        current_index, 1, QtWidgets.QTableWidgetItem(cnic)
                    )
                    self.admin_window.details_table.setItem(
                        current_index,
                        2,
                        QtWidgets.QTableWidgetItem(account["Account Number"]),
                    )
                    self.admin_window.details_table.setItem(
                        current_index,
                        3,
                        QtWidgets.QTableWidgetItem(account["Account Type"]),
                    )
                    self.admin_window.details_table.setItem(
                        current_index,
                        4,
                        QtWidgets.QTableWidgetItem(account["Account Number"]),
                    )
                    self.admin_window.details_table.setItem(
                        current_index,
                        5,
                        QtWidgets.QTableWidgetItem(account["Account Name"]),
                    )
                    self.admin_window.details_table.setItem(
                        current_index,
                        6,
                        QtWidgets.QTableWidgetItem(str(account["Net Pay"])),
                    )
                current_index += 1  


    def setupDB(self):
            from database import Hakoniwa

            self.userAccountInfo = Hakoniwa("DB.json")


    def searchRecord(self):
        search_item = self.admin_window.search.text()
        for row in range(self.admin_window.details_table.rowCount()):
            for col in range(self.admin_window.details_table.columnCount()):
                item = self.admin_window.details_table.item(row, col)
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
