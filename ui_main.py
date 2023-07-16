from PyQt5 import QtCore, QtGui, QtWidgets

class DashBoard:
    def setupDashboard(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(1200, 800)
        MainWindow.setMaximumSize(16777215, 16777215)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top_Bar.setStyleSheet("border:0.5px solid rgb(85, 170, 0)")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_toggle.setStyleSheet("QPushButton:hover {\n"
                                        "    background-color:#f1fcf3;\n"
                                        "    \n"
                                        "}")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Btn_Toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet("* {color: #f1fcf3;\n"
                                      "border: 0px solid;\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color:#f1fcf3;\n"
                                      "\n"
                                      "}")
        self.Btn_Toggle.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/burgur.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Toggle.setIcon(icon)
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        self.verticalLayout_2.addWidget(self.Btn_Toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        self.frame_top.setStyleSheet("QLabel{border:0}")
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.dashboard_top = QtWidgets.QLabel(self.frame_top)
        self.dashboard_top.setStyleSheet("font: 18pt \"Modern No. 20\";\n"
                                         "color:green;")
        self.dashboard_top.setObjectName("dashboard_top")
        self.horizontalLayout_9.addWidget(self.dashboard_top)
        self.name_top = QtWidgets.QLabel(self.frame_top)
        self.name_top.setStyleSheet("font: 18pt \"Modern No. 20\";\n"
                                    "color:green;")
        self.name_top.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.name_top.setObjectName("name_top")
        self.horizontalLayout_9.addWidget(self.name_top)
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(72, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_left_menu.setStyleSheet("*{background-color: rgb(255, 255, 255);\n"
                                           "border:2px solid rgb(85, 170, 0);\n"
                                           "border-top:0;}\n"
                                           "")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "border:0")
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_page_1 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_1.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_page_1.setStyleSheet("QPushButton {\n"
                                      "    color:black; font:13pt \"Modern No. 20\";\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "    border: 0px solid;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: #f1fcf3;\n"
                                      "}")
        self.btn_page_1.setText("")
        # self.btn_page_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/home.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_page_1.setIcon(icon1)
        self.btn_page_1.setObjectName("btn_page_1")
        self.verticalLayout_4.addWidget(self.btn_page_1)
        self.btn_page_2 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_2.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_page_2.setStyleSheet("QPushButton {\n"
                                      "    color:black; font:13pt \"Modern No. 20\";\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "    border: 0px solid;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: #f1fcf3;\n"
                                      "}")
        self.btn_page_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/card.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_page_2.setIcon(icon2)
        self.btn_page_2.setObjectName("btn_page_2")
        self.verticalLayout_4.addWidget(self.btn_page_2)
        self.btn_page_3 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_3.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_page_3.setStyleSheet("QPushButton {\n"
                                      "    color:black; font:13pt \"Modern No. 20\";\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "    border: 0px solid;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: #f1fcf3;\n"
                                      "}")
        self.btn_page_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/transactions.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_page_3.setIcon(icon3)
        self.btn_page_3.setObjectName("btn_page_3")
        self.verticalLayout_4.addWidget(self.btn_page_3)
        self.verticalLayout_3.addWidget(
        self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.logout_button =QtWidgets.QPushButton(self.frame_left_menu) 
        self.logout_button.setObjectName(u"logout")
        self.logout_button.setStyleSheet("QPushButton {\n"
                                      "    color:black; font:13pt \"Modern No. 20\";\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "    border: 0px solid;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: #f1fcf3;\n"
                                      "}")
        self.logout_button.setMinimumSize(QtCore.QSize(0, 40))
        self.logout_button.clicked.connect(self.logout)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/logout.png"))
        self.logout_button.setIcon(icon4)
        self.verticalLayout_3.addWidget(self.logout_button)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.responsivePages = QtWidgets.QStackedWidget(self.frame_pages)
        self.responsivePages.setObjectName("responsivePages")
        self.cardpage = QtWidgets.QWidget()
        self.cardpage.setObjectName("cardpage")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.cardpage)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.mainframe_card = QtWidgets.QFrame(self.cardpage)
        self.mainframe_card.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe_card.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe_card.setObjectName("mainframe_card")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.mainframe_card)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.card_frame = QtWidgets.QFrame(self.mainframe_card)
        self.card_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.card_frame.setStyleSheet("*{\n"
                                      "background-color:transparent;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "#card_frame{\n"
                                      "border-radius:30px;\n"
                                      "border:1.5px solid black;\n"
                                      "\n"
                                      "background-color: #28b44c;}")
        self.card_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card_frame.setObjectName("card_frame")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.card_frame)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.top_card = QtWidgets.QFrame(self.card_frame)
        self.top_card.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_card.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_card.setObjectName("top_card")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.top_card)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.company_name = QtWidgets.QLabel(self.top_card)
        self.company_name.setStyleSheet("color:white;\n"
                                        "font: 30pt \"Modern No. 20\";\n"
                                        "font-weight:1000;")
        self.company_name.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.company_name.setObjectName("company_name")
        self.horizontalLayout_12.addWidget(self.company_name)
        self.company_logo = QtWidgets.QLabel(self.top_card)
        self.company_logo.setText("")
        self.company_logo.setPixmap(
            QtGui.QPixmap("./icons/logo_card.png"))
        self.company_logo.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.company_logo.setObjectName("company_logo")
        self.horizontalLayout_12.addWidget(self.company_logo)
        self.verticalLayout_12.addWidget(self.top_card)
        self.acc_number = QtWidgets.QLabel(self.card_frame)
        self.acc_number.setStyleSheet("color:white;\n"
                                      "font: 40pt \"Modern No. 20\";\n"
                                      "font-weight:1000;")
        self.acc_number.setObjectName("acc_number")
        self.verticalLayout_12.addWidget(self.acc_number)
        self.card_holder = QtWidgets.QLabel(self.card_frame)
        self.card_holder.setMaximumSize(QtCore.QSize(16777215, 20))
        self.card_holder.setStyleSheet("color:gray;\n"
                                       "font: 15pt \"Modern No. 20\";\n"
                                       "font-weight:1000;")
        self.card_holder.setObjectName("card_holder")
        self.verticalLayout_12.addWidget(self.card_holder)
        self.name_expiry = QtWidgets.QFrame(self.card_frame)
        self.name_expiry.setMaximumSize(QtCore.QSize(16777215, 70))
        self.name_expiry.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name_expiry.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name_expiry.setObjectName("name_expiry")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.name_expiry)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.name_card = QtWidgets.QLabel(self.name_expiry)
        self.name_card.setStyleSheet("color:white;\n"
                                     "font: 30pt \"Modern No. 20\";\n"
                                     "font-weight:1000;")
        self.name_card.setObjectName("name_card")
        self.horizontalLayout_11.addWidget(self.name_card)
        self.expiry_date = QtWidgets.QLabel(self.name_expiry)
        self.expiry_date.setStyleSheet("color:white;\n"
                                       "font: 30pt \"Modern No. 20\";\n"
                                       "font-weight:1000;")
        self.expiry_date.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.expiry_date.setObjectName("expiry_date")
        self.horizontalLayout_11.addWidget(self.expiry_date)
        self.verticalLayout_12.addWidget(self.name_expiry)
        self.horizontalLayout_10.addWidget(self.card_frame)
        self.utility_frame = QtWidgets.QFrame(self.mainframe_card)
        self.utility_frame.setStyleSheet(
            "#utility_frame{border-left:3px solid gray;}")
        self.utility_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.utility_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.utility_frame.setObjectName("utility_frame")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.utility_frame)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.payment_details = QtWidgets.QFrame(self.utility_frame)
        self.payment_details.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.payment_details.setFrameShadow(QtWidgets.QFrame.Raised)
        self.payment_details.setObjectName("payment_details")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.payment_details)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.payment = QtWidgets.QLabel(self.payment_details)
        self.payment.setStyleSheet("font: 28pt \"Modern No. 20\";\n"
                                   "")
        self.payment.setObjectName("payment")
        self.verticalLayout_14.addWidget(self.payment)
        self.verticalLayout_13.addWidget(self.payment_details)
        self.name_number = QtWidgets.QFrame(self.utility_frame)
        self.name_number.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name_number.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name_number.setObjectName("name_number")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.name_number)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.number_2 = QtWidgets.QPushButton(self.name_number)
        self.number_2.setMinimumSize(QtCore.QSize(0, 40))
        self.number_2.setStyleSheet("border:2px solid black;\n"
                                    "font: 12pt \"Modern No. 20\";\n"
                                    "text-align:left;\n"
                                    "padding-left:5px;\n"
                                    "border-radius:7px;\n"
                                    "color:gray;\n"
                                    "")
        self.number_2.setObjectName("number_2")
        self.number_2.clicked.connect(self.number_copy)
        self.number_2.clicked.connect(lambda: self.buttonclick(self.number_2))
        self.verticalLayout_15.addWidget(self.number_2)
        self.name_2 = QtWidgets.QPushButton(self.name_number)
        self.name_2.setMinimumSize(QtCore.QSize(0, 40))
        self.name_2.setStyleSheet("border:2px solid black;\n"
                                  "font: 12pt \"Modern No. 20\";\n"
                                  "text-align:left;\n"
                                  "padding-left:5px;\n"
                                  "border-radius:7px;\n"
                                  "color:gray;\n"
                                  "")
        self.name_2.setObjectName("name_2")
        self.name_2.clicked.connect(self.name_copy)
        self.name_2.clicked.connect(lambda: self.buttonclick(self.name_2))
        self.verticalLayout_15.addWidget(self.name_2)
        
        self.verticalLayout_13.addWidget(self.name_number)
        self.expiry_card = QtWidgets.QFrame(self.utility_frame)
        self.expiry_card.setMaximumSize(QtCore.QSize(16777215, 70))
        self.expiry_card.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.expiry_card.setFrameShadow(QtWidgets.QFrame.Raised)
        self.expiry_card.setObjectName("expiry_card")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.expiry_card)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.month = QtWidgets.QPushButton(self.expiry_card)
        
        self.month.setMinimumSize(QtCore.QSize(0, 40))
        self.month.setStyleSheet("border:2px solid black;\n"
                                 "font: 12pt \"Modern No. 20\";\n"
                                 "text-align:left;\n"
                                 "padding-left:5px;\n"
                                 "border-radius:7px;\n"
                                 "color:gray;\n"
                                 "")
        
        self.month.setObjectName("month")
        self.month.clicked.connect(self.month_copy)
        self.month.clicked.connect(lambda: self.buttonclick(self.month))
        self.horizontalLayout_13.addWidget(self.month)
        self.year = QtWidgets.QPushButton(self.expiry_card)
        self.year.setMinimumSize(QtCore.QSize(0, 40))
        self.year.setStyleSheet("border:2px solid black;\n"
                                "font: 12pt \"Modern No. 20\";\n"
                                "text-align:left;\n"
                                "padding-left:5px;\n"
                                "border-radius:7px;\n"
                                "color:gray;\n"
                                "")
        self.year.setObjectName("year")
        self.year.clicked.connect(self.year_copy)
        self.year.clicked.connect(lambda: self.buttonclick(self.year))
        self.horizontalLayout_13.addWidget(self.year)
        self.verticalLayout_13.addWidget(self.expiry_card)
        self.buttons_for_card = QtWidgets.QFrame(self.utility_frame)
        self.buttons_for_card.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons_for_card.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons_for_card.setObjectName("buttons_for_card")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.buttons_for_card)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.copy = QtWidgets.QPushButton(self.buttons_for_card)
        self.copy.setMinimumSize(QtCore.QSize(150, 40))
        self.copy.setStyleSheet("border:2px solid black;\n"
                                "font: 12pt \"Modern No. 20\";\n"
                                "padding-left:5px;\n"
                                "border-radius:7px;\n"
                                "background-color:#28b44c;\n"
                                "")
        self.copy.setObjectName("copy")
        self.copy.clicked.connect(self.copy_details)
        self.copy.clicked.connect(lambda: self.buttonclick(self.copy))
        self.horizontalLayout_14.addWidget(self.copy)
        self.reveal = QtWidgets.QPushButton(self.buttons_for_card)
        self.reveal.setMinimumSize(QtCore.QSize(150, 40))
        self.reveal.setStyleSheet("border:2px solid black;\n"
                                  "font: 12pt \"Modern No. 20\";\n"
                                  "padding-left:5px;\n"
                                  "border-radius:7px;\n"
                                  "background-color:#28b44c;")
        self.reveal.setObjectName("reveal")
        self.reveal.clicked.connect(self.reveal_details)
        self.reveal.clicked.connect(lambda: self.buttonclick(self.reveal))
        self.horizontalLayout_14.addWidget(self.reveal)
        self.verticalLayout_13.addWidget(self.buttons_for_card)
        self.horizontalLayout_10.addWidget(self.utility_frame)
        self.verticalLayout_7.addWidget(self.mainframe_card)
        self.responsivePages.addWidget(self.cardpage)
        self.mainDashBoard = QtWidgets.QWidget()
        self.mainDashBoard.setObjectName("mainDashBoard")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.mainDashBoard)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.mainframe_dash = QtWidgets.QFrame(self.mainDashBoard)
        self.mainframe_dash.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe_dash.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe_dash.setObjectName("mainframe_dash")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.mainframe_dash)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.card = QtWidgets.QFrame(self.mainframe_dash)
        self.card.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card.setObjectName("card")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.card)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.credit_card = QtWidgets.QFrame(self.card)
        self.credit_card.setStyleSheet("#credit_card {\n"
                                       "\n"
                                       "border-radius:10px; border:1px solid black;\n"
                                       "background-image:url(icons/k83TfhGe_2x.jpg);\n"
                                       "background-repeat: no-repeat;\n"
                                       "  background-position: top;\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "}")
        self.credit_card.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.credit_card.setFrameShadow(QtWidgets.QFrame.Raised)
        self.credit_card.setObjectName("credit_card")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.credit_card)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.bank_name_logo = QtWidgets.QFrame(self.credit_card)
        self.bank_name_logo.setStyleSheet("background-color:transparent;")
        self.bank_name_logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bank_name_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bank_name_logo.setObjectName("bank_name_logo")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.bank_name_logo)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.name = QtWidgets.QLabel(self.bank_name_logo)
        self.name.setStyleSheet("color:white; \n"
                                "font: 35pt \"Modern No. 20\";\n"
                                "font-weight:700;")
        self.name.setAlignment(QtCore.Qt.AlignLeading |
                               QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.name.setObjectName("name")
        self.horizontalLayout_6.addWidget(self.name)
        self.logo = QtWidgets.QLabel(self.bank_name_logo)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("./icons/logo_card.png"))
        self.logo.setAlignment(QtCore.Qt.AlignRight |
                               QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        self.logo.setObjectName("logo")
        self.horizontalLayout_6.addWidget(self.logo)
        self.verticalLayout_10.addWidget(self.bank_name_logo)
        self.number_expiry = QtWidgets.QFrame(self.credit_card)
        self.number_expiry.setStyleSheet("background-color:transparent;")
        self.number_expiry.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.number_expiry.setFrameShadow(QtWidgets.QFrame.Raised)
        self.number_expiry.setObjectName("number_expiry")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.number_expiry)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.number = QtWidgets.QLabel(self.number_expiry)
        self.number.setStyleSheet("color:#008817;\n"
                                  "font: 28pt \"Modern No. 20\";")
        self.number.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.number.setObjectName("number")
        self.horizontalLayout_5.addWidget(self.number)
        self.expiry = QtWidgets.QLabel(self.number_expiry)
        self.expiry.setStyleSheet("color:#008817;\n"
                                  "font: 18pt \"Modern No. 20\";")
        self.expiry.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.expiry.setObjectName("expiry")
        self.horizontalLayout_5.addWidget(self.expiry)
        self.verticalLayout_10.addWidget(self.number_expiry)
        self.horizontalLayout_3.addWidget(self.credit_card)
        self.balance_frame = QtWidgets.QFrame(self.card)
        self.balance_frame.setStyleSheet(
            "#balance_frame{border-left:2px solid gray;}")
        self.balance_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.balance_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.balance_frame.setObjectName("balance_frame")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.balance_frame)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.balance = QtWidgets.QFrame(self.balance_frame)
        self.balance.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.balance.setFrameShadow(QtWidgets.QFrame.Raised)
        self.balance.setObjectName("balance")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.balance)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.balance_label = QtWidgets.QLabel(self.balance)
        self.balance_label.setStyleSheet("font: 24pt \"Modern No. 20\";")
        self.balance_label.setObjectName("balance_label")
        self.horizontalLayout_4.addWidget(self.balance_label)
        self.verticalLayout_11.addWidget(self.balance)
        self.money = QtWidgets.QFrame(self.balance_frame)
        self.money.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.money.setFrameShadow(QtWidgets.QFrame.Raised)
        self.money.setObjectName("money")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.money)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.money_label = QtWidgets.QLabel(self.money)
        self.money_label.setStyleSheet("color:green;\n"
                                       "font: 24pt \"Modern No. 20\";")
        self.money_label.setObjectName("money_label")
        self.horizontalLayout_7.addWidget(self.money_label)
        self.verticalLayout_11.addWidget(self.money)
        self.average = QtWidgets.QFrame(self.balance_frame)
        self.average.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.average.setFrameShadow(QtWidgets.QFrame.Raised)
        self.average.setObjectName("average")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.average)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.income = QtWidgets.QLabel(self.average)
        self.income.setStyleSheet("font: 18pt \"Modern No. 20\";\n"
                                  "color:green;")
        self.income.setObjectName("income")
        self.horizontalLayout_8.addWidget(self.income)
        self.expense = QtWidgets.QLabel(self.average)
        self.expense.setStyleSheet("font: 18pt \"Modern No. 20\";\n"
                                   "color:#CD5C5C;")
        self.expense.setObjectName("expense")
        self.horizontalLayout_8.addWidget(self.expense)
        self.verticalLayout_11.addWidget(self.average)
        self.horizontalLayout_3.addWidget(self.balance_frame)
        self.verticalLayout_9.addWidget(self.card)
        self.transactions = QtWidgets.QFrame(self.mainframe_dash)
        self.transactions.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.transactions.setFrameShadow(QtWidgets.QFrame.Raised)
        self.transactions.setObjectName("transactions")   
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.transactions)
        self.transaction_1 = QtWidgets.QFrame(self.transactions)
        self.transaction_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.transaction_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.transaction_1.setObjectName("transaction_1")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.transaction_1)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.amount_1 = QtWidgets.QLabel(self.transaction_1)
        self.amount_1.setObjectName("amount_1")
        self.horizontalLayout_19.addWidget(self.amount_1)
        self.details_1 = QtWidgets.QFrame(self.transaction_1)
        self.details_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.details_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.details_1.setObjectName("details_1")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.details_1)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.withdrawn_1 = QtWidgets.QLabel(self.details_1)
        self.withdrawn_1.setObjectName("withdrawn_1")
        self.verticalLayout_25.addWidget(self.withdrawn_1)
        self.date_1 = QtWidgets.QLabel(self.details_1)
        self.date_1.setObjectName("date_1")
        self.verticalLayout_25.addWidget(self.date_1)
        self.horizontalLayout_19.addWidget(self.details_1)
        
        self.transaction_2 = QtWidgets.QFrame(self.transactions)
        self.transaction_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.transaction_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.transaction_2.setObjectName("transaction_2")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.transaction_2)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.amount_2 = QtWidgets.QLabel(self.transaction_2)
        self.amount_2.setObjectName("amount_2")
        self.horizontalLayout_18.addWidget(self.amount_2)
        self.details_2 = QtWidgets.QFrame(self.transaction_2)
        self.details_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.details_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.details_2.setObjectName("details_2")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.details_2)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.withdraw_2 = QtWidgets.QLabel(self.details_2)
        self.withdraw_2.setObjectName("withdraw_2")
        self.verticalLayout_24.addWidget(self.withdraw_2)
        self.date_2 = QtWidgets.QLabel(self.details_2)
        self.date_2.setObjectName("date_2")
        self.verticalLayout_24.addWidget(self.date_2)
        self.horizontalLayout_18.addWidget(self.details_2)
        
        self.transaction_3 = QtWidgets.QFrame(self.transactions)
        self.transaction_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.transaction_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.transaction_3.setObjectName("transaction_3")
        
        self.transaction_1.setStyleSheet("#transaction_1 {border: 1px solid black;border-radius: 20px;padding-left:30px} *{font: 15pt \"Modern No. 20\";}")
        self.transaction_2.setStyleSheet("#transaction_2 {border: 1px solid black;border-radius: 20px;padding-left:30px} *{font: 15pt \"Modern No. 20\";}")
        self.transaction_3.setStyleSheet("#transaction_3 {border: 1px solid black;border-radius: 20px;padding-left:30px} *{font: 15pt \"Modern No. 20\";}")
        self.no_transactions = QtWidgets.QLabel(self.transactions)
        self.no_transactions.setObjectName("no_transactions")
        self.no_transactions.setStyleSheet(
            'color:green;font: 24pt "Modern No. 20";'
        )
        self.no_transactions.setAlignment(QtCore.Qt.AlignCenter)
        self.no_transactions.setText("Transactions Made will show here.")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.transaction_3)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.amount_3 = QtWidgets.QLabel(self.transaction_3)
        self.amount_3.setObjectName("amount_3")
        self.horizontalLayout_20.addWidget(self.amount_3)
        self.details_3 = QtWidgets.QFrame(self.transaction_3)
        self.details_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.details_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.details_3.setObjectName("details_3")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.details_3)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.withdraw_3 = QtWidgets.QLabel(self.details_3)
        self.withdraw_3.setObjectName("withdraw_3")
        self.verticalLayout_26.addWidget(self.withdraw_3)
        self.date_3 = QtWidgets.QLabel(self.details_3)
        self.date_3.setObjectName("date_3")
        self.verticalLayout_26.addWidget(self.date_3)
        self.horizontalLayout_20.addWidget(self.details_3)
        self.verticalLayout_9.addWidget(self.transactions)
        
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        
        
        self.verticalLayout_6.addWidget(self.mainframe_dash)
        self.responsivePages.addWidget(self.mainDashBoard)
        self.Transactions = QtWidgets.QWidget()
        self.Transactions.setObjectName("Transactions")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.Transactions)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.main_frame_transactions = QtWidgets.QFrame(self.Transactions)
        self.main_frame_transactions.setFrameShape(
            QtWidgets.QFrame.StyledPanel)
        self.main_frame_transactions.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame_transactions.setObjectName("main_frame_transactions")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(
            self.main_frame_transactions)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.withdraw_deposit = QtWidgets.QFrame(self.main_frame_transactions)
        self.withdraw_deposit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.withdraw_deposit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.withdraw_deposit.setObjectName("withdraw_deposit")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.withdraw_deposit)
        self.verticalLayout_16.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_16.setSpacing(9)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.Balance = QtWidgets.QFrame(self.withdraw_deposit)
        self.Balance.setMaximumSize(QtCore.QSize(16777215, 100))
        self.Balance.setStyleSheet("border-bottom:3px dotted gray;")
        self.Balance.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Balance.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Balance.setObjectName("Balance")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.Balance)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.balance_label_tramsaction = QtWidgets.QLabel(self.Balance)
        self.balance_label_tramsaction.setStyleSheet("border:0;\n"
                                                     "border-radius:5px;\n"
                                                     "font: 25pt \"Modern No. 20\";\n"
                                                     "")
        self.balance_label_tramsaction.setObjectName(
            "balance_label_tramsaction")
        self.horizontalLayout_16.addWidget(self.balance_label_tramsaction)
        self.balance_amount = QtWidgets.QLabel(self.Balance)
        self.balance_amount.setStyleSheet("border:0;\n"
                                          "border-radius:5px;\n"
                                          "font: 25pt \"Modern No. 20\";\n"
                                          "")
        self.balance_amount.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.balance_amount.setObjectName("balance_amount")
        self.horizontalLayout_16.addWidget(self.balance_amount)
        self.overdraft = QtWidgets.QLabel(self.Balance)
        self.overdraft.setStyleSheet(
            "color:green;border:0;border-radius:5px;font: 25pt \"Modern No. 20\";")
        self.overdraft.setObjectName("overdraft")
        self.horizontalLayout_16.addWidget(self.overdraft)
        self.verticalLayout_16.addWidget(self.Balance)
        self.withdraw_frame = QtWidgets.QFrame(self.withdraw_deposit)
        self.withdraw_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.withdraw_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.withdraw_frame.setObjectName("withdraw_frame")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.withdraw_frame)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.deposit_frame = QtWidgets.QFrame(self.withdraw_frame)
        self.deposit_frame.setStyleSheet("border-bottom:3px dotted gray;")
        self.deposit_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.deposit_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.deposit_frame.setObjectName("deposit_frame")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.deposit_frame)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.deposit_label = QtWidgets.QLabel(self.deposit_frame)
        self.deposit_label.setStyleSheet("border:0;\n"
                                         "border-radius:5px;\n"
                                         "font: 25pt \"Modern No. 20\";\n"
                                         "color:green;\n"
                                         "")
        self.deposit_label.setObjectName("deposit_label")
        self.verticalLayout_18.addWidget(
            self.deposit_label, 0, QtCore.Qt.AlignHCenter)
        self.deposit_entry = QtWidgets.QLineEdit(self.deposit_frame)
        self.deposit_entry.setMinimumSize(QtCore.QSize(500, 100))
        self.deposit_entry.setStyleSheet("border:1px solid gray;\n"
                                         "border-radius:10px;\n"
                                         "font: 28pt \"Modern No. 20\";\n"
                                         "padding:12px;")
        self.deposit_entry.setText("")
        self.deposit_entry.setObjectName("deposit_entry")
        self.verticalLayout_18.addWidget(
            self.deposit_entry, 0, QtCore.Qt.AlignHCenter)
        self.deposit_entry.setValidator(QtGui.QRegExpValidator(
            QtCore.QRegExp("[0-9]{6}(?:\.[0-9]{10})?"), self.deposit_entry))
        self.deposit = QtWidgets.QPushButton(self.deposit_frame)
        self.deposit.setStyleSheet("border:2px solid black;\n"
                                   "border-radius:4px;\n"
                                   "font: 15pt \"Modern No. 20\";\n"
                                   "padding:6px 12px;\n"
                                   "background-color:#28b44c;")
        self.deposit.setObjectName("deposit")
        self.deposit.clicked.connect(lambda: self.buttonclick(self.deposit))
        self.deposit.clicked.connect(self.deposit_money)
        self.verticalLayout_18.addWidget(
            self.deposit, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_17.addWidget(self.deposit_frame)
        self.withdraw_entry = QtWidgets.QLabel(self.withdraw_frame)
        self.withdraw_entry.setStyleSheet("border:0;\n"
                                          "border-radius:5px;\n"
                                          "font: 25pt \"Modern No. 20\";\n"
                                          "color:green;\n"
                                          "")
        self.withdraw_entry.setObjectName("withdraw_entry")
        self.verticalLayout_17.addWidget(
            self.withdraw_entry, 0, QtCore.Qt.AlignHCenter)
        self.withdraw_label = QtWidgets.QLineEdit(self.withdraw_frame)
        self.withdraw_label.setMinimumSize(QtCore.QSize(500, 100))
        self.withdraw_label.setStyleSheet("border:1px solid gray;\n"
                                          "border-radius:10px;\n"
                                          "font: 28pt \"Modern No. 20\";\n"
                                          "padding:12px;")
        self.withdraw_label.setObjectName("withdraw_label")
        self.withdraw_label.setValidator(QtGui.QRegExpValidator(
            QtCore.QRegExp("[0-9]{6}(?:\.[0-9]{10})?"), self.withdraw_label))
        self.verticalLayout_17.addWidget(
            self.withdraw_label, 0, QtCore.Qt.AlignHCenter)
        self.withdraw = QtWidgets.QPushButton(self.withdraw_frame)
        self.withdraw.setStyleSheet("border:2px solid black;\n"
                                    "border-radius:4px;\n"
                                    "font: 15pt \"Modern No. 20\";\n"
                                    "padding:6px 12px;\n"
                                    "background-color:#28b44c;")
        self.withdraw.setObjectName("withdraw")
        self.withdraw.clicked.connect(lambda: self.buttonclick(self.withdraw))
        self.withdraw.clicked.connect(self.withdraw_money)
        self.verticalLayout_17.addWidget(
            self.withdraw, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_16.addWidget(self.withdraw_frame)
        self.horizontalLayout_15.addWidget(self.withdraw_deposit)
        self.transfer_frame = QtWidgets.QFrame(self.main_frame_transactions)
        self.transfer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.transfer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.transfer_frame.setObjectName("transfer_frame")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.transfer_frame)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.trasnsfer = QtWidgets.QFrame(self.transfer_frame)
        self.trasnsfer.setStyleSheet("border-bottom:3px dotted gray;")
        self.trasnsfer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.trasnsfer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.trasnsfer.setObjectName("trasnsfer")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.trasnsfer)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.transfer_label = QtWidgets.QLabel(self.trasnsfer)
        self.transfer_label.setStyleSheet("border:0;\n"
                                          "border-radius:5px;\n"
                                          "font: 25pt \"Modern No. 20\";\n"
                                          "color:green;\n"
                                          "")
        self.transfer_label.setObjectName("transfer_label")
        self.verticalLayout_20.addWidget(
            self.transfer_label, 0, QtCore.Qt.AlignHCenter)
        self.transfer_amount = QtWidgets.QLineEdit(self.trasnsfer)
        self.transfer_amount.setMinimumSize(QtCore.QSize(500, 100))
        self.transfer_amount.setStyleSheet("border:1px solid gray;\n"
                                           "border-radius:10px;\n"
                                           "font: 28pt \"Modern No. 20\";\n"
                                           "padding:12px;")
        self.transfer_amount.setValidator(QtGui.QRegExpValidator(
            QtCore.QRegExp("[0-9]{6}(?:\.[0-9]{10})?"), self.transfer_amount))
        self.transfer_amount.setText("")
        self.transfer_amount.setObjectName("transfer_amount")
        self.verticalLayout_20.addWidget(
            self.transfer_amount, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_19.addWidget(self.trasnsfer)
        self.select_label = QtWidgets.QLabel(self.transfer_frame)
        self.select_label.setStyleSheet("border:0;\n"
                                        "border-radius:5px;\n"
                                        "font: 25pt \"Modern No. 20\";\n"
                                        "color:green;\n"
                                        "")
        self.select_label.setObjectName("select_label")
        self.verticalLayout_19.addWidget(self.select_label)
        self.listofaccounts = QtWidgets.QComboBox(self.transfer_frame)
        self.listofaccounts.setStyleSheet("border:2px solid black;color: gray;border-radius:6px;padding:10px 6px;font: 18pt \"Modern No. 20\";\n"
                                          "")
        self.listofaccounts.setObjectName("listofaccounts")
        self.verticalLayout_19.addWidget(self.listofaccounts)
        self.transfer_button = QtWidgets.QPushButton(self.transfer_frame)
        self.transfer_button.setStyleSheet("border:2px solid black;\n"
                                           "border-radius:4px;\n"
                                           "font: 15pt \"Modern No. 20\";\n"
                                           "padding:6px 12px;\n"
                                           "background-color:#28b44c;")
        self.transfer_button.setObjectName("transfer_button")
        self.transfer_button.clicked.connect(
            lambda: self.buttonclick(self.transfer_button))
        self.transfer_button.clicked.connect(self.transfer_funds)
        self.verticalLayout_19.addWidget(
            self.transfer_button, 0, QtCore.Qt.AlignHCenter)
        self.generate_report = QtWidgets.QPushButton(self.transactions)
        self.generate_report.setMinimumHeight(30)
        self.generate_report.setStyleSheet('font: 20pt "Modern No. 20";color:blue;padding:3px 20px;border:2px solid darkblue;border-radius:5px;')
        self.generate_report.clicked.connect(self.generateReport)
        self.horizontalLayout_15.addWidget(self.transfer_frame)
        self.verticalLayout_8.addWidget(self.main_frame_transactions)
        self.responsivePages.addWidget(self.Transactions)
        self.verticalLayout_5.addWidget(self.responsivePages)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setWindowTitle("Dashboard")
        MainWindow.setCentralWidget(self.centralwidget)

        self.setDashboard(MainWindow)
        self.responsivePages.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def transfer_funds(self):
        pass
    def number_copy(self):
        pass
    def month_copy(self):
        pass
    def year_copy(self):
        pass
    def name_copy(self):
        pass
    def copy_details(self):
        pass
    def reveal_details(self):
        pass
    def deposit_money(self):
        pass
    def withdraw_money(self):
        pass
    def setDashboard(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.dashboard_top.setText(_translate("MainWindow", "Dashboard"))
        self.name_top.setText(_translate("MainWindow", "Welcome, Name here"))
        self.company_name.setText(_translate("MainWindow", "ETERNUS"))
        self.acc_number.setText(_translate("MainWindow", "number"))
        self.card_holder.setText(_translate("MainWindow", "Card Holder:"))
        self.name_card.setText(_translate("MainWindow", "Name"))
        self.expiry_date.setText(_translate("MainWindow", "23/09"))
        self.payment.setText(_translate("MainWindow", "Payment Details:"))
        self.number_2.setText(_translate("MainWindow", "Number"))
        self.name_2.setText(_translate("MainWindow", "Name"))
        self.month.setText(_translate("MainWindow", "month"))
        self.year.setText(_translate("MainWindow", "year"))
        self.copy.setText(_translate("MainWindow", "Copy Details"))
        self.reveal.setText(_translate("MainWindow", "Reveal"))
        self.name.setText(_translate("MainWindow", "ETERNUS"))
        self.number.setText(_translate("MainWindow", "123123-123123-123-123"))
        self.expiry.setText(_translate("MainWindow", "02/23"))
        self.balance_label.setText(_translate("MainWindow", "Balance:"))
        self.money_label.setText(_translate("MainWindow", "$203300"))
        self.income.setText(_translate("MainWindow", "Average Income:$12000"))
        self.expense.setText(_translate(
            "MainWindow", "Average Expense: $1200"))

        self.balance_label_tramsaction.setText(
            _translate("MainWindow", "Balance: "))
        self.balance_amount.setText(_translate("MainWindow", "$123123"))
        self.overdraft.setText(_translate("MainWindow", "+$200"))
        self.deposit_label.setText(_translate("MainWindow", "Deposit Amount:"))
        self.deposit_entry.setPlaceholderText(_translate("MainWindow", "$200"))
        self.deposit.setText(_translate("MainWindow", "Deposit"))
        self.withdraw_entry.setText(
            _translate("MainWindow", "Withdraw Amount:"))
        self.withdraw_label.setPlaceholderText(
            _translate("MainWindow", "$300"))
        self.withdraw.setText(_translate("MainWindow", "Withdraw"))
        self.transfer_label.setText(
            _translate("MainWindow", "Transfer Amount"))
        self.transfer_amount.setPlaceholderText(
            _translate("MainWindow", "$200"))
        self.select_label.setText(_translate(
            "MainWindow", "Select the account the transfer to:"))
        self.transfer_button.setText(_translate("MainWindow", "Transfer"))
        self.generate_report.setText(_translate("MainWindow", "Generate Report"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = DashBoard()
    ui.setupDashboard(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
