# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lab_2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1013, 561)
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Allods")
        self.city_label = QLabel(Form)
        self.city_label.setObjectName(u"city_label")
        self.city_label.setGeometry(QRect(40, 20, 171, 33))
        self.city_label.setStyleSheet(u"background-color: rgb(255, 255, 255, 50);\n"
"color: black;\n"
"font-weight: bold;\n"
"font-size: 15pt;")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(770, 20, 151, 41))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255, 10);\n"
"color: black;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(220, 20, 531, 41))
        self.lineEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 90);\n"
"border-radius: 15px;\n"
"border: 2px solid rgba(255, 255, 255, 200);")
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(250, 120, 341, 421))
        self.listWidget.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.address_label = QLabel(Form)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setGeometry(QRect(60, 120, 151, 31))
        self.address_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 90);\n"
"border-radius: 15px;\n"
"border: 2px solid rgba(255, 255, 255, 200);\n"
"font-size: 10pt;\n"
"")
        self.time_label = QLabel(Form)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setGeometry(QRect(10, 350, 131, 131))
        self.time_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 90);\n"
"border-radius: 15px;\n"
"border: 2px solid rgba(255, 255, 255, 200);\n"
"font-size: 10pt;")
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(630, 120, 351, 421))
        self.textEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.labelAdr = QLabel(Form)
        self.labelAdr.setObjectName(u"labelAdr")
        self.labelAdr.setGeometry(QRect(10, 125, 91, 21))
        self.labelAdr.setStyleSheet(u"background-color: rgb(255, 255, 255, 50);\n"
"color: black;\n"
"font-weight: bold;\n"
"font-size: 10pt;")
        self.labelTW = QLabel(Form)
        self.labelTW.setObjectName(u"labelTW")
        self.labelTW.setGeometry(QRect(20, 325, 111, 21))
        self.labelTW.setStyleSheet(u"background-color: rgb(255, 255, 255, 50);\n"
"color: black;\n"
"font-weight: bold;\n"
"font-size: 10pt;")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 100, 251, 20))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255, 50);\n"
"color: black;\n"
"font-weight: bold;\n"
"font-size: 10pt;")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(630, 100, 331, 20))
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255, 50);\n"
"color: black;\n"
"font-weight: bold;\n"
"font-size: 10pt;")

        self.retranslateUi(Form)
        self.lineEdit.returnPressed.connect(self.pushButton.click)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.city_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0433\u043e\u0440\u043e\u0434:</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"OK", None))
        self.address_label.setText("")
        self.time_label.setText("")
        self.labelAdr.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u0440\u0435\u0441:", None))
        self.labelTW.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f \u0440\u0430\u0431\u043e\u0442\u044b:", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u0435:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043e\u0431\u043c\u0435\u043d\u043e\u0432:", None))
    # retranslateUi

