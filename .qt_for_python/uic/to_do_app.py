# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'to_do_app.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(812, 646)
        MainWindow.setMinimumSize(QSize(754, 597))
        MainWindow.setStyleSheet(u"#search_Button{border : 0px;font: 11pt \"Yu Gothic UI\";}\n"
"#search_Button:hover{border : 0px;background-color: rgb(250, 251, 252);font: 11pt \"Yu Gothic UI\"}\n"
"#frame{background-color: rgb(255, 255, 255);}\n"
"#label{margin-left:5px;font: 10pt \"Yu Gothic UI\";}\n"
"#scrollAreaWidgetContents{\n"
"	background-color: rgb(255, 255, 255);}\n"
"#frame_17,#frame_2{ background-color: rgb(242, 231, 249);}\n"
"#label_2,#label_7,#label_8,#label_9,#label_10,#label_11,#label_12{\n"
"	font: 63 22pt \"Yu Gothic UI Semibold\";\n"
"	color: rgb(125, 82, 148);\n"
"}\n"
"#label_5{\n"
"  font: 75 16pt \"Yu Gothic UI Semiblod\";\n"
"	color: rgb(125, 82, 148);}\n"
"#label_3{\n"
"  font:  11pt \"Yu Gothic UI\";\n"
"	color: rgb(125, 82, 148);\n"
"}\n"
"#label_6{\n"
"  font:  11pt \"Yu Gothic UI\";\n"
"	color: rgb(125, 82, 148);\n"
"}\n"
"#pushButton,#pushButton_{border-radius:5px;\n"
"background-color: rgb(233, 219, 240);}\n"
"#pushButton:hover,#pushButton_:hover{border-radius:5px;\n"
"background-color: rgba(71, 71, 71,30);}\n"
""
                        "#frame_11{border-radius:10px;\n"
"background-color: rgba(255,255,255,0);}\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background-color: rgb(243, 243, 243);\n"
"    width: 5px;\n"
"    margin: 5px 0 5px 0;\n"
"	border-radius: 5px;\n"
" }\n"
"#frame_3{border:1px solid;}\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(180, 180, 180);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(180, 180, 180);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(180, 180, 180);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(180, 180, 180);\n"
"	height: 15px;\n"
"	border-top-left-radius: 2px;\n"
"	border-top-right-radius:2px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(180, 180, 180);\n"
"}\n"
"QScrollBar::sub-line:"
                        "vertical:pressed {	\n"
"	background-color: rgb(180, 180, 180);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(180, 180, 180);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 2px;\n"
"	border-bottom-right-radius: 2px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: rgb(180, 180, 180);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(180, 180, 180);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"#lineEdit{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(170, 85, 255);}\n"
"#action_{\n"
"	background-color: rgba(255, 255, 255, 0);border:none;}\n"
"#pushButton_x{background-color:rgba(255,255,255,0);border:1px solid;\n"
""
                        "border-color: rgb(125, 82, 148);border-radius:7px;\n"
"font: 10.5pt \"Yu Gothic UI\";color: rgb(125, 82, 148)}\n"
"\n"
"#pushButton_x:hover{background-color:rgba(71,71,71,20);border:1px solid;\n"
"border-color: rgb(125, 82, 148);border-radius:7px;\n"
"font: 10.5pt \"Yu Gothic UI\";color: rgb(125, 82, 148)}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame_3)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(250, 0))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.widget.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(230, 0))
        self.frame.setMaximumSize(QSize(230, 16777215))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 45))
        self.label.setMaximumSize(QSize(16777215, 45))
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 40))
        self.frame_5.setLayoutDirection(Qt.RightToLeft)
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.search_Button = QPushButton(self.frame_5)
        self.search_Button.setObjectName(u"search_Button")
        self.search_Button.setMinimumSize(QSize(40, 40))
        self.search_Button.setMaximumSize(QSize(40, 16777215))
        icon = QIcon()
        icon.addFile(u"../icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_Button.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.search_Button, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 208))
        self.frame_6.setMaximumSize(QSize(16777215, 208))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 9, 9, 9)
        self.line = QFrame(self.frame_7)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(180, 0))
        self.line.setMaximumSize(QSize(180, 16777215))
        self.line.setStyleSheet(u"color: rgb(232, 232, 234);")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout_6.addWidget(self.line, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 248))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(1)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.frame_4)

        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Sunken)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 230, 328))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.horizontalLayout_4.addWidget(self.frame)

        self.frame_17 = QFrame(self.widget)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_17)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_17)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 30))
        self.frame_8.setMaximumSize(QSize(16777215, 30))
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(352, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.minimize_btn = QPushButton(self.frame_8)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setMinimumSize(QSize(40, 31))
        self.minimize_btn.setStyleSheet(u"QPushButton{border:0px;\n"
"background-color: rgba(255, 255, 255, 0);}\n"
"QPushButton:hover{border:0px;\n"
"background-color: rgba(71, 71, 71,40);}")
        icon1 = QIcon()
        icon1.addFile(u"../icons/substract.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon1)
        self.minimize_btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.minimize_btn)

        self.maximize_btn = QPushButton(self.frame_8)
        self.maximize_btn.setObjectName(u"maximize_btn")
        self.maximize_btn.setMinimumSize(QSize(40, 31))
        self.maximize_btn.setStyleSheet(u"QPushButton{border:0px;\n"
"background-color: rgba(255, 255, 255, 0);}\n"
"QPushButton:hover{border:0px;background-color: rgba(71, 71, 71,40);}")
        icon2 = QIcon()
        icon2.addFile(u"../icons/square-shape-outline.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_btn.setIcon(icon2)
        self.maximize_btn.setIconSize(QSize(13, 16))

        self.horizontalLayout_2.addWidget(self.maximize_btn)

        self.close_btn = QPushButton(self.frame_8)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(40, 31))
        self.close_btn.setStyleSheet(u"QPushButton{border:0px;\n"
"background-color: rgba(255, 255, 255, 0);}\n"
"QPushButton:hover{border:0px;\n"
"background-color: rgb(200, 4, 17);}")
        icon3 = QIcon()
        icon3.addFile(u"../icons/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon3)
        self.close_btn.setIconSize(QSize(12, 16))

        self.horizontalLayout_2.addWidget(self.close_btn)


        self.verticalLayout_11.addWidget(self.frame_8)

        self.stackedWidget = QStackedWidget(self.frame_17)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.stackedWidget.setLineWidth(0)
        self.page_0 = QWidget()
        self.page_0.setObjectName(u"page_0")
        self.page_0.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.page_0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.page_0)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMinimumSize(QSize(0, 565))
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setSpacing(40)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SetMaximumSize)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(455, 100))
        self.frame_10.setMaximumSize(QSize(16777215, 100))
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(320, 0))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_14)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_2 = QLabel(self.frame_14)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_10.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_14)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 31))

        self.verticalLayout_10.addWidget(self.label_3)


        self.horizontalLayout_3.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(30, -1, 30, -1)
        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy1)
        self.frame_16.setMinimumSize(QSize(100, 0))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_ = QPushButton(self.frame_16)
        self.pushButton_.setObjectName(u"pushButton_")
        self.pushButton_.setMaximumSize(QSize(31, 31))
        icon4 = QIcon()
        icon4.addFile(u"../../../../Downloads/idee.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_.setIcon(icon4)
        self.pushButton_.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.pushButton_)

        self.pushButton = QPushButton(self.frame_16)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(31, 31))
        icon5 = QIcon()
        icon5.addFile(u"../icons/more.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon5)

        self.horizontalLayout_9.addWidget(self.pushButton)


        self.horizontalLayout_6.addWidget(self.frame_16)


        self.horizontalLayout_3.addWidget(self.frame_13, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy2)
        self.frame_11.setMinimumSize(QSize(300, 280))
        self.frame_11.setMaximumSize(QSize(300, 16777215))
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_11)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(9, 9, 9, 9)
        self.frame_18 = QFrame(self.frame_11)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(280, 290))
        self.frame_18.setMaximumSize(QSize(154548, 290))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_18)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_4 = QLabel(self.frame_18)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 128))
        self.label_4.setMaximumSize(QSize(128, 128))
        self.label_4.setPixmap(QPixmap(u"../../../../Downloads/task.png"))

        self.verticalLayout_13.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.label_5 = QLabel(self.frame_18)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(260, 100))

        self.verticalLayout_13.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.label_6 = QLabel(self.frame_18)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 16777215))
        self.label_6.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_13.addWidget(self.label_6)

        self.pushButton_x = QPushButton(self.frame_18)
        self.pushButton_x.setObjectName(u"pushButton_x")
        self.pushButton_x.setMinimumSize(QSize(0, 30))

        self.verticalLayout_13.addWidget(self.pushButton_x)


        self.verticalLayout_12.addWidget(self.frame_18)


        self.verticalLayout_9.addWidget(self.frame_11, 0, Qt.AlignHCenter)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 70))
        self.frame_12.setMaximumSize(QSize(16777215, 70))
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(15, -1, 15, -1)
        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(425, 50))
        self.frame_15.setMaximumSize(QSize(16777215, 50))
        self.frame_15.setMouseTracking(True)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_8.addWidget(self.frame_15)


        self.verticalLayout_9.addWidget(self.frame_12, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.frame_9)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_0)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_16 = QVBoxLayout(self.page_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.page_1)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_2 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)

        self.label_7 = QLabel(self.frame_21)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(400, 50))
        self.label_7.setMaximumSize(QSize(400, 50))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_7)

        self.horizontalSpacer_3 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)


        self.verticalLayout_16.addWidget(self.frame_21)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_17 = QVBoxLayout(self.page_2)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.page_2)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_4 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)

        self.label_8 = QLabel(self.frame_22)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(400, 50))
        self.label_8.setMaximumSize(QSize(400, 50))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_8)

        self.horizontalSpacer_5 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)


        self.verticalLayout_17.addWidget(self.frame_22)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_19 = QVBoxLayout(self.page_3)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.page_3)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_6 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_6)

        self.label_9 = QLabel(self.frame_24)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(400, 50))
        self.label_9.setMaximumSize(QSize(400, 50))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_9)

        self.horizontalSpacer_7 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_7)


        self.verticalLayout_19.addWidget(self.frame_24)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_18 = QVBoxLayout(self.page_4)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.page_4)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_8 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_8)

        self.label_10 = QLabel(self.frame_23)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(400, 50))
        self.label_10.setMaximumSize(QSize(400, 50))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_10)

        self.horizontalSpacer_9 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_9)


        self.verticalLayout_18.addWidget(self.frame_23)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_14 = QVBoxLayout(self.page_5)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.page_5)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_10 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_10)

        self.label_11 = QLabel(self.frame_19)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(400, 50))
        self.label_11.setMaximumSize(QSize(400, 50))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_11)

        self.horizontalSpacer_11 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_11)


        self.verticalLayout_14.addWidget(self.frame_19)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_15 = QVBoxLayout(self.page_6)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.page_6)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_12 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_12)

        self.label_12 = QLabel(self.frame_20)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(400, 50))
        self.label_12.setMaximumSize(QSize(400, 50))
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_12)

        self.horizontalSpacer_13 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_13)


        self.verticalLayout_15.addWidget(self.frame_20)

        self.stackedWidget.addWidget(self.page_6)

        self.verticalLayout_11.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.frame_17)


        self.horizontalLayout.addWidget(self.widget)


        self.verticalLayout_7.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"To Do App", None))
        self.search_Button.setText("")
        self.minimize_btn.setText("")
        self.maximize_btn.setText("")
        self.close_btn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ma journ\u00e9e", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"dimanche 15 aout ", None))
        self.pushButton_.setText("")
        self.pushButton.setText("")
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Concentrez-vous  sur votre \n"
"              journ\u00e9e", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Effectu\u00e9 des taches sur Ma journ\u00e9e,\n"
" une liste actualis\u00e9 touts les jours", None))
        self.pushButton_x.setText(QCoreApplication.translate("MainWindow", u"Ajouter la tache a Ma journ\u00e9e", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"En cours de Construction....", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"En cours de Construction....", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"En cours de Construction....", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"En cours de Construction....", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"En cours de Construction....", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"En cours de Construction....", None))
    # retranslateUi

