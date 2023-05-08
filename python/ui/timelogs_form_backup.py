# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timelogs_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(410, 804)
        MainWindow.setMinimumSize(QSize(410, 804))
        palette = QPalette()
        brush = QBrush(QColor(80, 80, 80, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(61, 16))
        font = QFont()
        font.setFamily(u"Quicksand")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label)

        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(331, 31))
        self.comboBox_2.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"font: 8pt \"Quicksand\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.comboBox_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(61, 16))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_4)

        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMinimumSize(QSize(0, 31))
        self.textEdit_2.setMaximumSize(QSize(16777215, 31))
        self.textEdit_2.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"font: 8pt \"Quicksand\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout.addWidget(self.textEdit_2)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(61, 16))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_6)

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"font: 8pt \"Quicksand\";\n"
"color: rgb(255, 255, 255);")
        self.spinBox.setMaximum(5000)

        self.verticalLayout.addWidget(self.spinBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_3)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(81, 21))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_7)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(331, 31))
        self.comboBox.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"font: 8pt \"Quicksand\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.comboBox)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_9)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_4)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(91, 21))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_8)

        self.textEdit_4 = QTextEdit(self.centralwidget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setMinimumSize(QSize(0, 101))
        self.textEdit_4.setMaximumSize(QSize(16777215, 101))
        self.textEdit_4.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"font: 8pt \"Quicksand\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.textEdit_4)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(61, 31))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(80, 80, 80);\n"
"font: 8pt \"Quicksand\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(111, 31))
        self.pushButton.setStyleSheet(u"background-color: rgb(41, 152, 255);\n"
"font: 8pt \"Quicksand\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Person", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Make sure to put your Shotgrid name or user.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Task", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ideally, the task that is related to your timestamp.", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Duration", None))
        self.spinBox.setSuffix(QCoreApplication.translate("MainWindow", u" minutes", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Select the category that most closely describes the nature of your timestamp.", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Optional text for specific description.", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Create Time Log", None))
    # retranslateUi

