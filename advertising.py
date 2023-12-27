# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'advertising.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import res_adv_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(402, 396)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread: pad, x1: 1, y1: 1, x2: 0, y2: 0, stop: 0 rgba(255, 0, 0, 255), stop: 0.427447 rgba(0, 128, 128, 255), stop: 1 rgba(255, 255, 0, 255));\n"
"font-family:Noto-Sans SC;")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 20, 321, 331))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.txt_Adv = QLabel(self.widget)
        self.txt_Adv.setObjectName(u"txt_Adv")
        self.txt_Adv.setStyleSheet(u"color:black;\n"
"font-weight:bold;\n"
"font-size:20pt;\n"
"background-color:none;\n"
"border:none;\n"
"")
        self.txt_Adv.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_Adv)

        self.choose_cat_type_Adv = QComboBox(self.widget)
        self.choose_cat_type_Adv.addItem("")
        self.choose_cat_type_Adv.addItem("")
        self.choose_cat_type_Adv.addItem("")
        self.choose_cat_type_Adv.setObjectName(u"choose_cat_type_Adv")
        self.choose_cat_type_Adv.setStyleSheet(u"QComboBox {\n"
"font-size:16pt;\n"
"color:black;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"color:black;\n"
"}")

        self.verticalLayout.addWidget(self.choose_cat_type_Adv)

        self.choose_name_Adv = QComboBox(self.widget)
        self.choose_name_Adv.addItem("")
        self.choose_name_Adv.addItem("")
        self.choose_name_Adv.addItem("")
        self.choose_name_Adv.addItem("")
        self.choose_name_Adv.addItem("")
        self.choose_name_Adv.addItem("")
        self.choose_name_Adv.addItem("")
        self.choose_name_Adv.addItem("")
        self.choose_name_Adv.addItem("")
        self.choose_name_Adv.setObjectName(u"choose_name_Adv")
        self.choose_name_Adv.setStyleSheet(u"QComboBox {\n"
"font-size:16pt;\n"
"color:black;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"color:black;\n"
"}")

        self.verticalLayout.addWidget(self.choose_name_Adv)

        self.choose_Adv = QComboBox(self.widget)
        self.choose_Adv.addItem("")
        self.choose_Adv.setObjectName(u"choose_Adv")
        self.choose_Adv.setStyleSheet(u"QComboBox {\n"
"font-size:16pt;\n"
"color:black;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"color:black;\n"
"}")

        self.verticalLayout.addWidget(self.choose_Adv)

        self.amount_Adv = QLineEdit(self.widget)
        self.amount_Adv.setObjectName(u"amount_Adv")
        self.amount_Adv.setStyleSheet(u"font-size:16pt;\n"
"color:black;\n"
"padding-left:10px;")

        self.verticalLayout.addWidget(self.amount_Adv)

        self.contacts_Adv = QLineEdit(self.widget)
        self.contacts_Adv.setObjectName(u"contacts_Adv")
        self.contacts_Adv.setStyleSheet(u"font-size:16pt;\n"
"color:black;\n"
"padding-left:10px;")

        self.verticalLayout.addWidget(self.contacts_Adv)

        self.button_Adv = QPushButton(self.widget)
        self.button_Adv.setObjectName(u"button_Adv")
        self.button_Adv.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    background-color: rgba(255, 255, 255, 30);\n"
"    border: 1px solid rgba(255, 255, 255, 40);\n"
"    border-radius: 7px;\n"
"    font-weight:bold;\n"
"    width: 170px;\n"
"    height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 255, 255, 70);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/add_box_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_Adv.setIcon(icon)

        self.verticalLayout.addWidget(self.button_Adv)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.choose_cat_type_Adv.setCurrentIndex(-1)
        self.choose_name_Adv.setCurrentIndex(-1)
        self.choose_Adv.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.txt_Adv.setText(QCoreApplication.translate("Dialog", u"Advertising", None))
        self.choose_cat_type_Adv.setItemText(0, QCoreApplication.translate("Dialog", u"Book", None))
        self.choose_cat_type_Adv.setItemText(1, QCoreApplication.translate("Dialog", u"Magazine", None))
        self.choose_cat_type_Adv.setItemText(2, QCoreApplication.translate("Dialog", u"Booklet", None))

        self.choose_cat_type_Adv.setPlaceholderText(QCoreApplication.translate("Dialog", u"Choose category", None))
        self.choose_name_Adv.setItemText(0, QCoreApplication.translate("Dialog", u"Mobi-Dick", None))
        self.choose_name_Adv.setItemText(1, QCoreApplication.translate("Dialog", u"Harry-Potter", None))
        self.choose_name_Adv.setItemText(2, QCoreApplication.translate("Dialog", u"Kobzar", None))
        self.choose_name_Adv.setItemText(3, QCoreApplication.translate("Dialog", u"New Times", None))
        self.choose_name_Adv.setItemText(4, QCoreApplication.translate("Dialog", u"Galka", None))
        self.choose_name_Adv.setItemText(5, QCoreApplication.translate("Dialog", u"Rada", None))
        self.choose_name_Adv.setItemText(6, QCoreApplication.translate("Dialog", u"Glovo", None))
        self.choose_name_Adv.setItemText(7, QCoreApplication.translate("Dialog", u"Blago", None))
        self.choose_name_Adv.setItemText(8, QCoreApplication.translate("Dialog", u"Ratusha", None))

        self.choose_name_Adv.setPlaceholderText(QCoreApplication.translate("Dialog", u"Choose category", None))
        self.choose_Adv.setItemText(0, QCoreApplication.translate("Dialog", u"Yes", None))

        self.choose_Adv.setPlaceholderText(QCoreApplication.translate("Dialog", u"Advertising", None))
        self.amount_Adv.setPlaceholderText(QCoreApplication.translate("Dialog", u"Amount", None))
        self.contacts_Adv.setPlaceholderText(QCoreApplication.translate("Dialog", u"Contacts", None))
        self.button_Adv.setText(QCoreApplication.translate("Dialog", u"Save", None))
    # retranslateUi

