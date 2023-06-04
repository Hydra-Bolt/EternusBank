# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'ui_mainvwoPQu.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc


class DashBoard(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 700)
        MainWindow.setMinimumSize(QSize(1200, 700))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"border:0.5px solid rgb(85, 170, 0)")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet("\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "	background-color:#f1fcf3;\n"
                                        "	\n"
                                        "}")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"* {color: #f1fcf3;\n"
                                      "border: 0px solid;\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "	background-color:#f1fcf3;\n"
                                      "\n"
                                      "}")
        icon = QIcon()
        icon.addFile(u"icons/7216128.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Toggle.setIcon(icon)

        self.verticalLayout_2.addWidget(self.Btn_Toggle)

        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setStyleSheet(u"QLabel{border:0}")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.dashboard_top = QLabel(self.frame_top)
        self.dashboard_top.setObjectName(u"dashboard_top")
        self.dashboard_top.setStyleSheet(u"font: 18pt \"Modern No. 20\";\n"
                                         "color:green;")

        self.horizontalLayout_9.addWidget(self.dashboard_top)

        self.name_top = QLabel(self.frame_top)
        self.name_top.setObjectName(u"name_top")
        self.name_top.setStyleSheet(u"font: 18pt \"Modern No. 20\";\n"
                                    "color:green;")
        self.name_top.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.name_top)

        self.horizontalLayout.addWidget(self.frame_top)

        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(72, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"*{background-color: rgb(255, 255, 255);\n"
                                           "border:2px solid rgb(85, 170, 0);\n"
                                           "border-top:0;}\n"
                                           "")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                           "border:0")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(0, 40))
        self.btn_page_1.setStyleSheet(u"QPushButton {\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "	background-color: rgb(255, 255, 255);\n"
                                      "	border: 0px solid;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "	background-color: #f1fcf3;\n"
                                      "}")
        icon1 = QIcon()
        icon1.addFile(u"icons/2427222.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_1.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.btn_page_1)

        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 40))
        self.btn_page_2.setStyleSheet(u"QPushButton {\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "	background-color: rgb(255, 255, 255);\n"
                                      "	border: 0px solid;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "	background-color: #f1fcf3;\n"
                                      "}")
        icon2 = QIcon()
        icon2.addFile(u"icons/62780.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_2.setIcon(icon2)

        self.verticalLayout_4.addWidget(self.btn_page_2)

        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 40))
        self.btn_page_3.setStyleSheet(u"QPushButton {\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "	background-color: rgb(255, 255, 255);\n"
                                      "	border: 0px solid;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "	background-color: #f1fcf3;\n"
                                      "}")
        icon3 = QIcon()
        icon3.addFile(u"icons/1751700.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_3.setIcon(icon3)

        self.verticalLayout_4.addWidget(self.btn_page_3)

        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)

        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.responsivePages = QStackedWidget(self.frame_pages)
        self.responsivePages.setObjectName(u"responsivePages")
        
        self.cardpage = QWidget()
        self.cardpage.setObjectName(u"cardpage")
        self.verticalLayout_7 = QVBoxLayout(self.cardpage)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.mainframe_card = QFrame(self.cardpage)
        self.mainframe_card.setObjectName(u"mainframe_card")
        self.mainframe_card.setFrameShape(QFrame.StyledPanel)
        self.mainframe_card.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.mainframe_card)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.card_frame = QFrame(self.mainframe_card)
        self.card_frame.setObjectName(u"card_frame")
        self.card_frame.setMaximumSize(QSize(16777215, 16777215))
        self.card_frame.setStyleSheet(u"*{\n"
                                      "background-color:transparent;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "#card_frame{\n"
                                      "border-radius:30px;\n"
                                      "border:1.5px solid black;\n"
                                      "\n"
                                      "background-color: #28b44c;}")
        self.card_frame.setFrameShape(QFrame.StyledPanel)
        self.card_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.card_frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.top_card = QFrame(self.card_frame)
        self.top_card.setObjectName(u"top_card")
        self.top_card.setFrameShape(QFrame.StyledPanel)
        self.top_card.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.top_card)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.company_name = QLabel(self.top_card)
        self.company_name.setObjectName(u"company_name")
        self.company_name.setStyleSheet(u"color:white;\n"
                                        "font: 30pt \"Modern No. 20\";\n"
                                        "font-weight:1000;")
        self.company_name.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.company_name)

        self.company_logo = QLabel(self.top_card)
        self.company_logo.setObjectName(u"company_logo")
        self.company_logo.setPixmap(QPixmap(u"E:/bankingApp/logo_card.png"))
        self.company_logo.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.company_logo)

        self.verticalLayout_12.addWidget(self.top_card)

        self.acc_number = QLabel(self.card_frame)
        self.acc_number.setObjectName(u"acc_number")
        self.acc_number.setStyleSheet(u"color:white;\n"
                                      "font: 40pt \"Modern No. 20\";\n"
                                      "font-weight:1000;")

        self.verticalLayout_12.addWidget(self.acc_number)

        self.card_holder = QLabel(self.card_frame)
        self.card_holder.setObjectName(u"card_holder")
        self.card_holder.setMaximumSize(QSize(16777215, 20))
        self.card_holder.setStyleSheet(u"color:gray;\n"
                                       "font: 15pt \"Modern No. 20\";\n"
                                       "font-weight:1000;")

        self.verticalLayout_12.addWidget(self.card_holder)

        self.name_expiry = QFrame(self.card_frame)
        self.name_expiry.setObjectName(u"name_expiry")
        self.name_expiry.setMaximumSize(QSize(16777215, 70))
        self.name_expiry.setFrameShape(QFrame.StyledPanel)
        self.name_expiry.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.name_expiry)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.name_card = QLabel(self.name_expiry)
        self.name_card.setObjectName(u"name_card")
        self.name_card.setStyleSheet(u"color:white;\n"
                                     "font: 30pt \"Modern No. 20\";\n"
                                     "font-weight:1000;")

        self.horizontalLayout_11.addWidget(self.name_card)

        self.expiry_date = QLabel(self.name_expiry)
        self.expiry_date.setObjectName(u"expiry_date")
        self.expiry_date.setStyleSheet(u"color:white;\n"
                                       "font: 30pt \"Modern No. 20\";\n"
                                       "font-weight:1000;")
        self.expiry_date.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.expiry_date)

        self.verticalLayout_12.addWidget(self.name_expiry)

        self.horizontalLayout_10.addWidget(self.card_frame)

        self.utility_frame = QFrame(self.mainframe_card)
        self.utility_frame.setObjectName(u"utility_frame")
        self.utility_frame.setStyleSheet(
            u"#utility_frame{border-left:3px solid gray;}")
        self.utility_frame.setFrameShape(QFrame.StyledPanel)
        self.utility_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.utility_frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.payment_details = QFrame(self.utility_frame)
        self.payment_details.setObjectName(u"payment_details")
        self.payment_details.setFrameShape(QFrame.StyledPanel)
        self.payment_details.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.payment_details)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.payment = QLabel(self.payment_details)
        self.payment.setObjectName(u"payment")
        self.payment.setStyleSheet(u"font: 28pt \"Modern No. 20\";\n"
                                   "")

        self.verticalLayout_14.addWidget(self.payment)

        self.verticalLayout_13.addWidget(self.payment_details)

        self.name_number = QFrame(self.utility_frame)
        self.name_number.setObjectName(u"name_number")
        self.name_number.setFrameShape(QFrame.StyledPanel)
        self.name_number.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.name_number)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.number_2 = QPushButton(self.name_number)
        self.number_2.setObjectName(u"number_2")
        self.number_2.setMinimumSize(QSize(0, 40))
        self.number_2.setStyleSheet(u"border:2px solid black;\n"
                                    "font: 12pt \"Modern No. 20\";\n"
                                    "text-align:left;\n"
                                    "padding-left:5px;\n"
                                    "border-radius:7px;\n"
                                    "color:gray;\n"
                                    "")

        self.verticalLayout_15.addWidget(self.number_2)

        self.name_2 = QPushButton(self.name_number)
        self.name_2.setObjectName(u"name_2")
        self.name_2.setMinimumSize(QSize(0, 40))
        self.name_2.setStyleSheet(u"border:2px solid black;\n"
                                  "font: 12pt \"Modern No. 20\";\n"
                                  "text-align:left;\n"
                                  "padding-left:5px;\n"
                                  "border-radius:7px;\n"
                                  "color:gray;\n"
                                  "")

        self.verticalLayout_15.addWidget(self.name_2)

        self.verticalLayout_13.addWidget(self.name_number)

        self.expiry_card = QFrame(self.utility_frame)
        self.expiry_card.setObjectName(u"expiry_card")
        self.expiry_card.setMaximumSize(QSize(16777215, 70))
        self.expiry_card.setFrameShape(QFrame.StyledPanel)
        self.expiry_card.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.expiry_card)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.month = QPushButton(self.expiry_card)
        self.month.setObjectName(u"month")
        self.month.setMinimumSize(QSize(0, 40))
        self.month.setStyleSheet(u"border:2px solid black;\n"
                                 "font: 12pt \"Modern No. 20\";\n"
                                 "text-align:left;\n"
                                 "padding-left:5px;\n"
                                 "border-radius:7px;\n"
                                 "color:gray;\n"
                                 "")

        self.horizontalLayout_13.addWidget(self.month)

        self.year = QPushButton(self.expiry_card)
        self.year.setObjectName(u"year")
        self.year.setMinimumSize(QSize(0, 40))
        self.year.setStyleSheet(u"border:2px solid black;\n"
                                "font: 12pt \"Modern No. 20\";\n"
                                "text-align:left;\n"
                                "padding-left:5px;\n"
                                "border-radius:7px;\n"
                                "color:gray;\n"
                                "")

        self.horizontalLayout_13.addWidget(self.year)

        self.verticalLayout_13.addWidget(self.expiry_card)

        self.buttons_for_card = QFrame(self.utility_frame)
        self.buttons_for_card.setObjectName(u"buttons_for_card")
        self.buttons_for_card.setFrameShape(QFrame.StyledPanel)
        self.buttons_for_card.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.buttons_for_card)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.copy = QPushButton(self.buttons_for_card)
        self.copy.setObjectName(u"copy")
        self.copy.setMinimumSize(QSize(150, 40))
        self.copy.setStyleSheet(u"border:2px solid black;\n"
                                "font: 12pt \"Modern No. 20\";\n"
                                "padding-left:5px;\n"
                                "border-radius:7px;\n"
                                "background-color:#28b44c;\n"
                                "")

        self.horizontalLayout_14.addWidget(self.copy)

        self.reveal = QPushButton(self.buttons_for_card)
        self.reveal.setObjectName(u"reveal")
        self.reveal.setMinimumSize(QSize(150, 40))
        self.reveal.setStyleSheet(u"border:2px solid black;\n"
                                  "font: 12pt \"Modern No. 20\";\n"
                                  "padding-left:5px;\n"
                                  "border-radius:7px;\n"
                                  "background-color:#28b44c;")

        self.horizontalLayout_14.addWidget(self.reveal)

        self.verticalLayout_13.addWidget(self.buttons_for_card)

        self.horizontalLayout_10.addWidget(self.utility_frame)

        self.verticalLayout_7.addWidget(self.mainframe_card)

        self.responsivePages.addWidget(self.cardpage)
        self.mainDashBoard = QWidget()
        self.mainDashBoard.setObjectName(u"mainDashBoard")
        self.verticalLayout_6 = QVBoxLayout(self.mainDashBoard)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.mainframe_dash = QFrame(self.mainDashBoard)
        self.mainframe_dash.setObjectName(u"mainframe_dash")
        self.mainframe_dash.setFrameShape(QFrame.StyledPanel)
        self.mainframe_dash.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.mainframe_dash)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.card = QFrame(self.mainframe_dash)
        self.card.setObjectName(u"card")
        self.card.setFrameShape(QFrame.StyledPanel)
        self.card.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.card)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.credit_card = QFrame(self.card)
        self.credit_card.setObjectName(u"credit_card")
        self.credit_card.setStyleSheet(u"#credit_card {\n"
                                       "\n"
                                       "border-radius:10px;\n"
                                       "background-image:url(icons/k83TfhGe_2x.jpg);\n"
                                       "background-repeat: no-repeat;\n"
                                       "  background-position: top;\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "}")
        self.credit_card.setFrameShape(QFrame.StyledPanel)
        self.credit_card.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.credit_card)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.bank_name_logo = QFrame(self.credit_card)
        self.bank_name_logo.setObjectName(u"bank_name_logo")
        self.bank_name_logo.setStyleSheet(u"background-color:transparent;")
        self.bank_name_logo.setFrameShape(QFrame.StyledPanel)
        self.bank_name_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.bank_name_logo)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.name = QLabel(self.bank_name_logo)
        self.name.setObjectName(u"name")
        self.name.setStyleSheet(u"color:white; \n"
                                "font: 35pt \"Modern No. 20\";\n"
                                "font-weight:700;")
        self.name.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.horizontalLayout_6.addWidget(self.name)

        self.logo = QLabel(self.bank_name_logo)
        self.logo.setObjectName(u"logo")
        self.logo.setPixmap(QPixmap(u"E:/bankingApp/logo_card.png"))
        self.logo.setAlignment(Qt.AlignRight | Qt.AlignTop | Qt.AlignTrailing)

        self.horizontalLayout_6.addWidget(self.logo)

        self.verticalLayout_10.addWidget(self.bank_name_logo)

        self.number_expiry = QFrame(self.credit_card)
        self.number_expiry.setObjectName(u"number_expiry")
        self.number_expiry.setStyleSheet(u"background-color:transparent;")
        self.number_expiry.setFrameShape(QFrame.StyledPanel)
        self.number_expiry.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.number_expiry)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.number = QLabel(self.number_expiry)
        self.number.setObjectName(u"number")
        self.number.setStyleSheet(u"color:#008817;\n"
                                  "font: 28pt \"Modern No. 20\";")
        self.number.setAlignment(
            Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)

        self.horizontalLayout_5.addWidget(self.number)

        self.expiry = QLabel(self.number_expiry)
        self.expiry.setObjectName(u"expiry")
        self.expiry.setStyleSheet(u"color:#008817;\n"
                                  "font: 18pt \"Modern No. 20\";")
        self.expiry.setAlignment(
            Qt.AlignBottom | Qt.AlignRight | Qt.AlignTrailing)

        self.horizontalLayout_5.addWidget(self.expiry)

        self.verticalLayout_10.addWidget(self.number_expiry)

        self.horizontalLayout_3.addWidget(self.credit_card)

        self.balance_frame = QFrame(self.card)
        self.balance_frame.setObjectName(u"balance_frame")
        self.balance_frame.setStyleSheet(
            u"#balance_frame{border-left:2px solid gray;}")
        self.balance_frame.setFrameShape(QFrame.StyledPanel)
        self.balance_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.balance_frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.balance = QFrame(self.balance_frame)
        self.balance.setObjectName(u"balance")
        self.balance.setFrameShape(QFrame.StyledPanel)
        self.balance.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.balance)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.balance_label = QLabel(self.balance)
        self.balance_label.setObjectName(u"balance_label")
        self.balance_label.setStyleSheet(u"font: 24pt \"Modern No. 20\";")

        self.horizontalLayout_4.addWidget(self.balance_label)

        self.verticalLayout_11.addWidget(self.balance)

        self.money = QFrame(self.balance_frame)
        self.money.setObjectName(u"money")
        self.money.setFrameShape(QFrame.StyledPanel)
        self.money.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.money)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.money_label = QLabel(self.money)
        self.money_label.setObjectName(u"money_label")
        self.money_label.setStyleSheet(u"color:green;\n"
                                       "font: 24pt \"Modern No. 20\";")

        self.horizontalLayout_7.addWidget(self.money_label)

        self.verticalLayout_11.addWidget(self.money)

        self.average = QFrame(self.balance_frame)
        self.average.setObjectName(u"average")
        self.average.setFrameShape(QFrame.StyledPanel)
        self.average.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.average)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.income = QLabel(self.average)
        self.income.setObjectName(u"income")
        self.income.setStyleSheet(u"font: 18pt \"Modern No. 20\";\n"
                                  "color:green;")

        self.horizontalLayout_8.addWidget(self.income)

        self.expense = QLabel(self.average)
        self.expense.setObjectName(u"expense")
        self.expense.setStyleSheet(u"font: 18pt \"Modern No. 20\";\n"
                                   "color:#CD5C5C;")

        self.horizontalLayout_8.addWidget(self.expense)

        self.verticalLayout_11.addWidget(self.average)

        self.horizontalLayout_3.addWidget(self.balance_frame)

        self.verticalLayout_9.addWidget(self.card)

        self.transactions = QFrame(self.mainframe_dash)
        self.transactions.setObjectName(u"transactions")
        self.transactions.setFrameShape(QFrame.StyledPanel)
        self.transactions.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.transactions)

        self.verticalLayout_6.addWidget(self.mainframe_dash)

        self.responsivePages.addWidget(self.mainDashBoard)
        self.Transactions = QWidget()
        self.Transactions.setObjectName(u"Transactions")
        self.verticalLayout_8 = QVBoxLayout(self.Transactions)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.main_frame_transactions = QFrame(self.Transactions)
        self.main_frame_transactions.setObjectName(u"main_frame_transactions")
        self.main_frame_transactions.setFrameShape(QFrame.StyledPanel)
        self.main_frame_transactions.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.main_frame_transactions)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.withdraw_deposit = QFrame(self.main_frame_transactions)
        self.withdraw_deposit.setObjectName(u"withdraw_deposit")
        self.withdraw_deposit.setFrameShape(QFrame.StyledPanel)
        self.withdraw_deposit.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.withdraw_deposit)
        self.verticalLayout_16.setSpacing(9)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(9, 9, 9, 9)
        self.Balance = QFrame(self.withdraw_deposit)
        self.Balance.setObjectName(u"Balance")
        self.Balance.setMaximumSize(QSize(16777215, 100))
        self.Balance.setStyleSheet(u"border-bottom:3px dotted gray;")
        self.Balance.setFrameShape(QFrame.StyledPanel)
        self.Balance.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.Balance)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.balance_label_tramsaction = QLabel(self.Balance)
        self.balance_label_tramsaction.setObjectName(
            u"balance_label_tramsaction")
        self.balance_label_tramsaction.setStyleSheet(u"border:0;\n"
                                                     "border-radius:5px;\n"
                                                     "font: 25pt \"Modern No. 20\";\n"
                                                     "")

        self.horizontalLayout_16.addWidget(self.balance_label_tramsaction)

        self.balance_amount = QLabel(self.Balance)
        self.balance_amount.setObjectName(u"balance_amount")
        self.balance_amount.setStyleSheet(u"border:0;\n"
                                          "border-radius:5px;\n"
                                          "font: 25pt \"Modern No. 20\";\n"
                                          "")
        self.balance_amount.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.balance_amount)

        self.overdraft = QLabel(self.Balance)
        self.overdraft.setObjectName(u"label")
        self.overdraft.setStyleSheet(
            u"color:green;border:0;border-radius:5px;font: 25pt \"Modern No. 20\";")

        self.horizontalLayout_16.addWidget(self.overdraft)

        self.verticalLayout_16.addWidget(self.Balance)

        self.withdraw_frame = QFrame(self.withdraw_deposit)
        self.withdraw_frame.setObjectName(u"withdraw_frame")
        self.withdraw_frame.setFrameShape(QFrame.StyledPanel)
        self.withdraw_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.withdraw_frame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.deposit_frame = QFrame(self.withdraw_frame)
        self.deposit_frame.setObjectName(u"deposit_frame")
        self.deposit_frame.setStyleSheet(u"border-bottom:3px dotted gray;")
        self.deposit_frame.setFrameShape(QFrame.StyledPanel)
        self.deposit_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.deposit_frame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.deposit_label = QLabel(self.deposit_frame)
        self.deposit_label.setObjectName(u"deposit_label")
        self.deposit_label.setStyleSheet(u"border:0;\n"
                                         "border-radius:5px;\n"
                                         "font: 25pt \"Modern No. 20\";\n"
                                         "color:green;\n"
                                         "")

        self.verticalLayout_18.addWidget(
            self.deposit_label, 0, Qt.AlignHCenter)

        self.deposit_entry = QLineEdit(self.deposit_frame)
        self.deposit_entry.setObjectName(u"deposit_entry")
        self.deposit_entry.setMinimumSize(QSize(500, 100))
        self.deposit_entry.setStyleSheet(u"border:1px solid gray;\n"
                                         "border-radius:10px;\n"
                                         "font: 28pt \"Modern No. 20\";\n"
                                         "padding:12px;")

        self.verticalLayout_18.addWidget(
            self.deposit_entry, 0, Qt.AlignHCenter)

        self.deposit = QPushButton(self.deposit_frame)
        self.deposit.setObjectName(u"deposit")
        self.deposit.setStyleSheet(u"border:2px solid black;\n"
                                   "border-radius:4px;\n"
                                   "font: 15pt \"Modern No. 20\";\n"
                                   "padding:6px 12px;\n"
                                   "background-color:#28b44c;")

        self.verticalLayout_18.addWidget(self.deposit, 0, Qt.AlignHCenter)

        self.verticalLayout_17.addWidget(self.deposit_frame)

        self.withdraw_entry = QLabel(self.withdraw_frame)
        self.withdraw_entry.setObjectName(u"withdraw_entry")
        self.withdraw_entry.setStyleSheet(u"border:0;\n"
                                          "border-radius:5px;\n"
                                          "font: 25pt \"Modern No. 20\";\n"
                                          "color:green;\n"
                                          "")

        self.verticalLayout_17.addWidget(
            self.withdraw_entry, 0, Qt.AlignHCenter)

        self.withdraw_label = QLineEdit(self.withdraw_frame)
        self.withdraw_label.setObjectName(u"withdraw_label")
        self.withdraw_label.setMinimumSize(QSize(500, 100))
        self.withdraw_label.setStyleSheet(u"border:1px solid gray;\n"
                                          "border-radius:10px;\n"
                                          "font: 28pt \"Modern No. 20\";\n"
                                          "padding:12px;")

        self.verticalLayout_17.addWidget(
            self.withdraw_label, 0, Qt.AlignHCenter)

        self.withdraw = QPushButton(self.withdraw_frame)
        self.withdraw.setObjectName(u"withdraw")
        self.withdraw.setStyleSheet(u"border:2px solid black;\n"
                                    "border-radius:4px;\n"
                                    "font: 15pt \"Modern No. 20\";\n"
                                    "padding:6px 12px;\n"
                                    "background-color:#28b44c;")

        self.verticalLayout_17.addWidget(self.withdraw, 0, Qt.AlignHCenter)

        self.verticalLayout_16.addWidget(self.withdraw_frame)

        self.horizontalLayout_15.addWidget(self.withdraw_deposit)

        self.transfer_frame = QFrame(self.main_frame_transactions)
        self.transfer_frame.setObjectName(u"transfer_frame")
        self.transfer_frame.setFrameShape(QFrame.StyledPanel)
        self.transfer_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.transfer_frame)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.trasnsfer = QFrame(self.transfer_frame)
        self.trasnsfer.setObjectName(u"trasnsfer")
        self.trasnsfer.setStyleSheet(u"border-bottom:3px dotted gray;")
        self.trasnsfer.setFrameShape(QFrame.StyledPanel)
        self.trasnsfer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.trasnsfer)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.transfer_label = QLabel(self.trasnsfer)
        self.transfer_label.setObjectName(u"transfer_label")
        self.transfer_label.setStyleSheet(u"border:0;\n"
                                          "border-radius:5px;\n"
                                          "font: 25pt \"Modern No. 20\";\n"
                                          "color:green;\n"
                                          "")

        self.verticalLayout_20.addWidget(
            self.transfer_label, 0, Qt.AlignHCenter)

        self.transfer_amount = QLineEdit(self.trasnsfer)
        self.transfer_amount.setObjectName(u"transfer_amount")
        self.transfer_amount.setMinimumSize(QSize(500, 100))
        self.transfer_amount.setStyleSheet(u"border:1px solid gray;\n"
                                           "border-radius:10px;\n"
                                           "font: 28pt \"Modern No. 20\";\n"
                                           "padding:12px;")

        self.verticalLayout_20.addWidget(
            self.transfer_amount, 0, Qt.AlignHCenter)

        self.verticalLayout_22.addWidget(self.trasnsfer)

        self.select_label = QLabel(self.transfer_frame)
        self.select_label.setObjectName(u"select_label")
        self.select_label.setStyleSheet(u"border:0;\n"
                                        "border-radius:5px;\n"
                                        "font: 25pt \"Modern No. 20\";\n"
                                        "color:green;\n"
                                        "")

        self.verticalLayout_22.addWidget(self.select_label, 0, Qt.AlignHCenter)

        self.listofaccounts = QComboBox(self.transfer_frame)
        self.listofaccounts.setObjectName(u"listofaccounts")
        self.listofaccounts.setStyleSheet(u"border:2px solid black;color: gray;border-radius:6px;padding:10px 6px;font: 18pt \"Modern No. 20\";\n"
                                          "")

        self.verticalLayout_22.addWidget(self.listofaccounts)

        self.horizontalLayout_15.addWidget(self.transfer_frame)

        self.verticalLayout_8.addWidget(self.main_frame_transactions)

        self.responsivePages.addWidget(self.Transactions)

        self.verticalLayout_5.addWidget(self.responsivePages)

        self.horizontalLayout_2.addWidget(self.frame_pages)

        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.responsivePages.setCurrentIndex(2)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText("")
        self.dashboard_top.setText(QCoreApplication.translate(
            "MainWindow", u"Dashboard", None))
        self.name_top.setText(QCoreApplication.translate(
            "MainWindow", u"Welcome, Name here", None))
        self.btn_page_1.setText("")
        self.btn_page_2.setText("")
        self.btn_page_3.setText("")
        self.company_name.setText(
            QCoreApplication.translate("MainWindow", u"ETERNUS", None))
        self.company_logo.setText("")
        self.acc_number.setText(QCoreApplication.translate(
            "MainWindow", u"number", None))
        self.card_holder.setText(QCoreApplication.translate(
            "MainWindow", u"Card Holder:", None))
        self.name_card.setText(
            QCoreApplication.translate("MainWindow", u"Name", None))
        self.expiry_date.setText(
            QCoreApplication.translate("MainWindow", u"23/09", None))
        self.payment.setText(QCoreApplication.translate(
            "MainWindow", u"Payment Details:", None))
        self.number_2.setText(QCoreApplication.translate(
            "MainWindow", u"Number", None))
        self.name_2.setText(QCoreApplication.translate(
            "MainWindow", u"Name", None))
        self.month.setText(QCoreApplication.translate(
            "MainWindow", u"month", None))
        self.year.setText(QCoreApplication.translate(
            "MainWindow", u"year", None))
        self.copy.setText(QCoreApplication.translate(
            "MainWindow", u"Copy Details", None))
        self.reveal.setText(QCoreApplication.translate(
            "MainWindow", u"Reveal", None))
        self.name.setText(QCoreApplication.translate(
            "MainWindow", u"ETERNUS", None))
        self.logo.setText("")
        self.number.setText(QCoreApplication.translate(
            "MainWindow", u"123123-123123-123-123", None))
        self.expiry.setText(QCoreApplication.translate(
            "MainWindow", u"02/23", None))
        self.balance_label.setText(
            QCoreApplication.translate("MainWindow", u"Balance:", None))
        self.money_label.setText(QCoreApplication.translate(
            "MainWindow", u"$203300", None))
        self.income.setText(QCoreApplication.translate(
            "MainWindow", u"Average Income:$12000", None))
        self.expense.setText(QCoreApplication.translate(
            "MainWindow", u"Average Expense: $1200", None))
        self.balance_label_tramsaction.setText(
            QCoreApplication.translate("MainWindow", u"Balance: ", None))
        self.balance_amount.setText(
            QCoreApplication.translate("MainWindow", u"$123123", None))
        self.overdraft.setText(QCoreApplication.translate(
            "MainWindow", u"+$200", None))
        self.deposit_label.setText(QCoreApplication.translate(
            "MainWindow", u"Deposit Amount:", None))
        self.deposit_entry.setText("")
        self.deposit_entry.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"$200", None))
        self.deposit.setText(QCoreApplication.translate(
            "MainWindow", u"Deposit", None))
        self.withdraw_entry.setText(QCoreApplication.translate(
            "MainWindow", u"Withdraw Amount:", None))
        self.withdraw_label.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"$300", None))
        self.withdraw.setText(QCoreApplication.translate(
            "MainWindow", u"Withdraw", None))
        self.transfer_label.setText(QCoreApplication.translate(
            "MainWindow", u"Transfer Amount", None))
        self.transfer_amount.setText("")
        self.transfer_amount.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"$200", None))
        self.select_label.setText(QCoreApplication.translate(
            "MainWindow", u"Select the account the transfer to:", None))
    # retranslateUi
