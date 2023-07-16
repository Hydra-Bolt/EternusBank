import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QMainWindow
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setRowCount(20)

        self.populate_table()

        self.setCentralWidget(self.table)

    def populate_table(self):
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                item = QTableWidgetItem(f"Row {row+1}, Column {col+1}")
                self.table.setItem(row, col, item)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        table_width = self.centralWidget().width() - self.table.verticalScrollBar().width()
        column_width = table_width // self.table.columnCount()

        for col in range(self.table.columnCount()):
            self.table.setColumnWidth(col, column_width)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
