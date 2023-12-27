# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transaction.ui'
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
import res_new_trans_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 455)
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
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 20, 331, 391))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.txt_Nt = QLabel(self.layoutWidget)
        self.txt_Nt.setObjectName(u"txt_Nt")
        self.txt_Nt.setStyleSheet(u"color:black;\n"
"font-weight:bold;\n"
"font-size:20pt;\n"
"background-color:none;\n"
"border:none;\n"
"")
        self.txt_Nt.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_Nt)

        self.choose_cat_Nt = QComboBox(self.layoutWidget)
        self.choose_cat_Nt.addItem("")
        self.choose_cat_Nt.addItem("")
        self.choose_cat_Nt.addItem("")
        self.choose_cat_Nt.setObjectName(u"choose_cat_Nt")
        self.choose_cat_Nt.setStyleSheet(u"QComboBox {\n"
"font-size:16pt;\n"
"color:black;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"color:black;\n"
"}")
        self.choose_cat_Nt.setMaxVisibleItems(10)

        self.verticalLayout.addWidget(self.choose_cat_Nt)

        self.name_Nt = QLineEdit(self.layoutWidget)
        self.name_Nt.setObjectName(u"name_Nt")
        self.name_Nt.setStyleSheet(u"font-size:16pt;\n"
"color:black;\n"
"padding-left:10px;")

        self.verticalLayout.addWidget(self.name_Nt)

        self.adv_Nt = QComboBox(self.layoutWidget)
        self.adv_Nt.addItem("")
        self.adv_Nt.setObjectName(u"adv_Nt")
        self.adv_Nt.setStyleSheet(u"QComboBox {\n"
"font-size:16pt;\n"
"color:black;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"color:black;\n"
"}")

        self.verticalLayout.addWidget(self.adv_Nt)

        self.amount_Nt = QLineEdit(self.layoutWidget)
        self.amount_Nt.setObjectName(u"amount_Nt")
        self.amount_Nt.setStyleSheet(u"font-size:16pt;\n"
"color:black;\n"
"padding-left:10px;")

        self.verticalLayout.addWidget(self.amount_Nt)

        self.contacts_Nt = QLineEdit(self.layoutWidget)
        self.contacts_Nt.setObjectName(u"contacts_Nt")
        self.contacts_Nt.setStyleSheet(u"font-size:16pt;\n"
"color:black;\n"
"padding-left:10px;")

        self.verticalLayout.addWidget(self.contacts_Nt)

        self.button_Nt = QPushButton(self.layoutWidget)
        self.button_Nt.setObjectName(u"button_Nt")
        self.button_Nt.setStyleSheet(u"QPushButton {\n"
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
        icon.addFile(u":/icon/icons/add_box_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_Nt.setIcon(icon)

        self.verticalLayout.addWidget(self.button_Nt)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.choose_cat_Nt.setCurrentIndex(0)
        self.adv_Nt.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.txt_Nt.setText(QCoreApplication.translate("Dialog", u"New transaction", None))
        self.choose_cat_Nt.setItemText(0, QCoreApplication.translate("Dialog", u"Book", None))
        self.choose_cat_Nt.setItemText(1, QCoreApplication.translate("Dialog", u"Magazine", None))
        self.choose_cat_Nt.setItemText(2, QCoreApplication.translate("Dialog", u"Booklet", None))

        self.choose_cat_Nt.setProperty("placeholderText", QCoreApplication.translate("Dialog", u"Choose category", None))
        self.name_Nt.setPlaceholderText(QCoreApplication.translate("Dialog", u"Name", None))
        self.adv_Nt.setItemText(0, QCoreApplication.translate("Dialog", u"No", None))

        self.adv_Nt.setProperty("placeholderText", QCoreApplication.translate("Dialog", u"Advertising", None))
        self.amount_Nt.setPlaceholderText(QCoreApplication.translate("Dialog", u"Amount", None))
        self.contacts_Nt.setPlaceholderText(QCoreApplication.translate("Dialog", u"Contacts", None))
        self.button_Nt.setText(QCoreApplication.translate("Dialog", u"Save transaction", None))
    # retranslateUi

