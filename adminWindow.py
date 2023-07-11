from PyQt5 import QtCore, QtGui, QtWidgets

class AdminWindow:
    def setup_AWindowUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1098, 644)
        MainWindow.setStyleSheet("background-color:white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_frame = QtWidgets.QFrame(self.centralwidget)
        self.top_frame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.top_frame.setStyleSheet("#top_frame{border:1.5px solid gray;}*{font: 16pt \"Modern No. 20\";color:green;}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.admin_window = QtWidgets.QLabel(self.top_frame)
        self.admin_window.setObjectName("admin_window")
        self.horizontalLayout.addWidget(self.admin_window)
        self.hello = QtWidgets.QLabel(self.top_frame)
        self.hello.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hello.setObjectName("hello")
        self.horizontalLayout.addWidget(self.hello)
        self.verticalLayout.addWidget(self.top_frame)
        self.search = QtWidgets.QLineEdit(self.centralwidget)
        self.search.setMaximumSize(QtCore.QSize(16777215, 40))
        self.search.setStyleSheet("font: 16pt \"Modern No. 20\";color:green;padding-left:3px;")
        self.search.setObjectName("search")
        self.verticalLayout.addWidget(self.search)
        self.details_frame = QtWidgets.QFrame(self.centralwidget)
        self.details_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.details_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.details_frame.setObjectName("details_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.details_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.details_table = QtWidgets.QTableWidget(self.details_frame)
        self.details_table.setStyleSheet("font: 16pt \"Modern No. 20\";color:green;")
        self.details_table.setShowGrid(True)
        self.details_table.setGridStyle(QtCore.Qt.DashLine)
        self.details_table.setCornerButtonEnabled(True)
        self.details_table.setObjectName("details_table")
        self.details_table.horizontalHeader().setDefaultSectionSize(150)
        self.details_table.horizontalHeader().setMinimumSectionSize(50)
        self.details_table.verticalHeader().setStretchLastSection(False)
        self.details_table.cellChanged.connect(self.updateRecords)
        self.verticalLayout_2.addWidget(self.details_table)
        self.button_frame = QtWidgets.QFrame(self.details_frame)
        self.button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame.setObjectName("button_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.button_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.delete_records = QtWidgets.QPushButton(self.button_frame)
        self.delete_records.setStyleSheet("font: 20pt \"Modern No. 20\";color:red;padding:3px 20px;border:2px solid darkred;border-radius:5px;")
        self.delete_records.setObjectName("delete_records")
        self.delete_records.clicked.connect(self.deleteRecords)
        self.generate_report = QtWidgets.QPushButton(self.button_frame)
        self.generate_report.setStyleSheet("font: 20pt \"Modern No. 20\";color:blue;padding:3px 20px;border:2px solid darkblue;border-radius:5px;")     
        self.generate_report.clicked.connect(self.generateReport)
        self.horizontalLayout_2.addWidget(self.generate_report)
        self.horizontalLayout_2.addWidget(self.delete_records)
        self.verticalLayout_2.addWidget(self.button_frame)
        self.verticalLayout.addWidget(self.details_frame)
        self.admin_window.setText("Admin Window")
        self.hello.setText("Hello There")
        self.search.setPlaceholderText("Search...")
        self.search.textChanged.connect(self.searchRecord)
        self.delete_records.setText("Delete Record")
        self.generate_report.setText("Generate Report")
        MainWindow.setCentralWidget(self.centralwidget)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def deleteRecords(self):
        pass
    
    def updateRecords(self):
        pass
    
    def generateReport(self):
        pass
    
    def searchRecord(self):
        pass
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AdminWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
