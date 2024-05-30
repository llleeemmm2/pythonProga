# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui6_LabThreeEditingWindow.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(538, 508)
        Dialog.setStyleSheet(u"background-color: #0000FF;")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(80, 450, 181, 32))
        self.buttonBox.setStyleSheet(u"background-color: rgb(255, 255, 255, 10);\n"
"color: black;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
        self.genreBox = QComboBox(Dialog)
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.addItem("")
        self.genreBox.setObjectName(u"genreBox")
        self.genreBox.setGeometry(QRect(20, 210, 191, 31))
        self.genreBox.setStyleSheet(u"background-color: rgba(255, 255, 255, 90);\n"
"border-radius: 15px;\n"
"border: 2px solid rgba(255, 255, 255, 200);")
        self.titleEdit = QLineEdit(Dialog)
        self.titleEdit.setObjectName(u"titleEdit")
        self.titleEdit.setGeometry(QRect(20, 120, 491, 31))
        self.titleEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 90);\n"
"border-radius: 15px;\n"
"border: 2px solid rgba(255, 255, 255, 200);")
        self.title = QLabel(Dialog)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(20, 90, 201, 31))
        self.title.setStyleSheet(u"background-color: rgb(255, 255, 255, 50);\n"
"color: black;\n"
"font-weight: bold;\n"
"font-size: 15pt;")
        self.genre = QLabel(Dialog)
        self.genre.setObjectName(u"genre")
        self.genre.setGeometry(QRect(20, 170, 181, 21))
        self.genre.setStyleSheet(u"background-color: rgb(255, 255, 255, 50);\n"
"color: black;\n"
"font-weight: bold;\n"
"font-size: 15pt")
        self.year = QLabel(Dialog)
        self.year.setObjectName(u"year")
        self.year.setGeometry(QRect(20, 270, 231, 16))
        self.year.setStyleSheet(u"background-color: rgb(255, 255, 255, 50);\n"
"color: black;\n"
"font-weight: bold;\n"
"font-size: 15pt;")
        self.duration = QLabel(Dialog)
        self.duration.setObjectName(u"duration")
        self.duration.setGeometry(QRect(20, 360, 261, 16))
        self.duration.setStyleSheet(u"background-color: rgb(255, 255, 255, 50);\n"
"color: black;\n"
"font-weight: bold;\n"
"font-size: 15pt;")
        self.yearEdit = QLineEdit(Dialog)
        self.yearEdit.setObjectName(u"yearEdit")
        self.yearEdit.setGeometry(QRect(20, 300, 271, 31))
        self.yearEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 90);\n"
"border-radius: 15px;\n"
"border: 2px solid rgba(255, 255, 255, 200);")
        self.durationEdit = QLineEdit(Dialog)
        self.durationEdit.setObjectName(u"durationEdit")
        self.durationEdit.setGeometry(QRect(20, 390, 321, 31))
        self.durationEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 90);\n"
"border-radius: 15px;\n"
"border: 2px solid rgba(255, 255, 255, 200);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 451, 31))
        self.label.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.genreBox.setItemText(0, QCoreApplication.translate("Dialog", u"\u043a\u043e\u043c\u0435\u0434\u0438\u044f", None))
        self.genreBox.setItemText(1, QCoreApplication.translate("Dialog", u"\u0434\u0440\u0430\u043c\u0430", None))
        self.genreBox.setItemText(2, QCoreApplication.translate("Dialog", u"\u043c\u0435\u043b\u043e\u0434\u0440\u0430\u043c\u0430", None))
        self.genreBox.setItemText(3, QCoreApplication.translate("Dialog", u"\u0434\u0435\u0442\u0435\u043a\u0442\u0438\u0432", None))
        self.genreBox.setItemText(4, QCoreApplication.translate("Dialog", u"\u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u043b\u044c\u043d\u044b\u0439", None))
        self.genreBox.setItemText(5, QCoreApplication.translate("Dialog", u"\u0443\u0436\u0430\u0441\u044b", None))
        self.genreBox.setItemText(6, QCoreApplication.translate("Dialog", u"\u043c\u0443\u0437\u044b\u043a\u0430", None))
        self.genreBox.setItemText(7, QCoreApplication.translate("Dialog", u"\u0444\u0430\u043d\u0442\u0430\u0441\u0442\u0438\u043a\u0430", None))
        self.genreBox.setItemText(8, QCoreApplication.translate("Dialog", u"\u0430\u043d\u0438\u043c\u0430\u0446\u0438\u044f", None))
        self.genreBox.setItemText(9, QCoreApplication.translate("Dialog", u"\u0431\u0438\u043e\u0433\u0440\u0430\u0444\u0438\u044f", None))
        self.genreBox.setItemText(10, QCoreApplication.translate("Dialog", u"\u0431\u043e\u0435\u0432\u0438\u043a", None))
        self.genreBox.setItemText(11, QCoreApplication.translate("Dialog", u"\u043f\u0440\u0438\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f", None))
        self.genreBox.setItemText(12, QCoreApplication.translate("Dialog", u"\u0432\u043e\u0439\u043d\u0430", None))
        self.genreBox.setItemText(13, QCoreApplication.translate("Dialog", u"\u0441\u0435\u043c\u0435\u0439\u043d\u044b\u0439", None))
        self.genreBox.setItemText(14, QCoreApplication.translate("Dialog", u"\u0442\u0440\u0438\u043b\u043b\u0435\u0440", None))
        self.genreBox.setItemText(15, QCoreApplication.translate("Dialog", u"\u0444\u044d\u043d\u0442\u0435\u0437\u0438", None))
        self.genreBox.setItemText(16, QCoreApplication.translate("Dialog", u"\u0432\u0435\u0441\u0442\u0435\u0440\u043d", None))
        self.genreBox.setItemText(17, QCoreApplication.translate("Dialog", u"\u043c\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.genreBox.setItemText(18, QCoreApplication.translate("Dialog", u"\u043a\u043e\u0440\u043e\u0442\u043a\u043e\u043c\u0435\u0442\u0440\u0430\u0436\u043d\u044b\u0439", None))
        self.genreBox.setItemText(19, QCoreApplication.translate("Dialog", u"\u043c\u044e\u0437\u0438\u043a\u043b", None))
        self.genreBox.setItemText(20, QCoreApplication.translate("Dialog", u"\u0438\u0441\u0442\u043e\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0439", None))
        self.genreBox.setItemText(21, QCoreApplication.translate("Dialog", u"\u043d\u0443\u0430\u0440", None))

        self.title.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.genre.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0436\u0430\u043d\u0440:", None))
        self.year.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0433\u043e\u0434 \u0432\u044b\u043f\u0443\u0441\u043a\u0430:", None))
        self.duration.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435  \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"           \u041e\u043a\u043d\u043e \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
    # retranslateUi

