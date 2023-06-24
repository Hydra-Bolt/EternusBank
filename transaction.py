import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class TransactionWidget(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.amountLabel = QtWidgets.QLabel(self)
        self.amountLabel.setObjectName("amountLabel")
        self.horizontalLayout.addWidget(self.amountLabel)

        self.detailsFrame = QtWidgets.QFrame(self)
        self.detailsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.detailsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.detailsFrame.setObjectName("detailsFrame")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.detailsFrame)
        self.verticalLayout.setObjectName("verticalLayout")

        self.withdrawnLabel = QtWidgets.QLabel(self.detailsFrame)
        self.withdrawnLabel.setObjectName("withdrawnLabel")
        self.verticalLayout.addWidget(self.withdrawnLabel)

        self.dateLabel = QtWidgets.QLabel(self.detailsFrame)
        self.dateLabel.setObjectName("dateLabel")
        self.verticalLayout.addWidget(self.dateLabel)

        self.horizontalLayout.addWidget(self.detailsFrame)

        self.setLayout(self.horizontalLayout)

