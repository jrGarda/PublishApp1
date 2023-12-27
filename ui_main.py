# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(784, 584)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread: pad, x1: 1, y1: 1, x2: 0, y2: 0, stop: 0 rgba(255, 0, 0, 255), stop: 0.427447 rgba(0, 128, 128, 255), stop: 1 rgba(255, 255, 0, 255));\n"
"font-family:Noto-Sans SC;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 750, 551))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.balance_frame = QFrame(self.widget)
        self.balance_frame.setObjectName(u"balance_frame")
        self.balance_frame.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.verticalLayout = QVBoxLayout(self.balance_frame)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.txt = QLabel(self.balance_frame)
        self.txt.setObjectName(u"txt")
        self.txt.setStyleSheet(u"color:black;\n"
"font-weight:bold;\n"
"font-size:20pt;\n"
"background-color:none;\n"
"border:none;\n"
"margin-bottom:50px\n"
"")

        self.verticalLayout.addWidget(self.txt)

        self.money_bal = QLabel(self.balance_frame)
        self.money_bal.setObjectName(u"money_bal")
        self.money_bal.setStyleSheet(u"color:black;\n"
"font-size:30pt;\n"
"background-color:none;\n"
"border:none;")

        self.verticalLayout.addWidget(self.money_bal)


        self.horizontalLayout_5.addWidget(self.balance_frame)

        self.price_frame = QFrame(self.widget)
        self.price_frame.setObjectName(u"price_frame")
        self.price_frame.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.verticalLayout_2 = QVBoxLayout(self.price_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.txt_price = QLabel(self.price_frame)
        self.txt_price.setObjectName(u"txt_price")
        self.txt_price.setStyleSheet(u"color:black;\n"
"font-weight:bold;\n"
"font-size:20pt;\n"
"background-color:none;\n"
"border:none;")

        self.verticalLayout_2.addWidget(self.txt_price)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.icon_own = QLabel(self.price_frame)
        self.icon_own.setObjectName(u"icon_own")
        self.icon_own.setMaximumSize(QSize(24, 16777215))
        self.icon_own.setStyleSheet(u"background-color:none;\n"
"border:none;")
        self.icon_own.setPixmap(QPixmap(u":/icon/icons/style_FILL0_wght400_GRAD0_opsz24.svg"))

        self.horizontalLayout_4.addWidget(self.icon_own)

        self.name_own = QLabel(self.price_frame)
        self.name_own.setObjectName(u"name_own")
        self.name_own.setStyleSheet(u"color:black;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color:none;\n"
"border:none;")

        self.horizontalLayout_4.addWidget(self.name_own)

        self.money_own = QLabel(self.price_frame)
        self.money_own.setObjectName(u"money_own")
        self.money_own.setMinimumSize(QSize(0, 0))
        self.money_own.setMaximumSize(QSize(1677, 16777215))
        self.money_own.setStyleSheet(u"color:black;\n"
"font-size: 16pt;\n"
"background-color:none;\n"
"border:none;\n"
"margin-left:20px;")
        self.money_own.setLineWidth(1)
        self.money_own.setWordWrap(True)
        self.money_own.setMargin(1)
        self.money_own.setIndent(-1)

        self.horizontalLayout_4.addWidget(self.money_own)

        self.per1pc_4 = QLabel(self.price_frame)
        self.per1pc_4.setObjectName(u"per1pc_4")
        self.per1pc_4.setStyleSheet(u"color:black;\n"
"font-size: 12pt;\n"
"background-color:none;\n"
"border:none;\n"
"margin-left:2px;")

        self.horizontalLayout_4.addWidget(self.per1pc_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.txt_advertising = QLabel(self.price_frame)
        self.txt_advertising.setObjectName(u"txt_advertising")
        self.txt_advertising.setStyleSheet(u"color:black;\n"
"font-weight:bold;\n"
"font-size:14pt;\n"
"background-color:none;\n"
"border:none;")

        self.verticalLayout_2.addWidget(self.txt_advertising)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.icon_book = QLabel(self.price_frame)
        self.icon_book.setObjectName(u"icon_book")
        self.icon_book.setMaximumSize(QSize(24, 16777215))
        self.icon_book.setStyleSheet(u"background-color:none;\n"
"border:none;")
        self.icon_book.setPixmap(QPixmap(u":/icon/icons/library_books_FILL0_wght400_GRAD0_opsz24.svg"))

        self.horizontalLayout_3.addWidget(self.icon_book)

        self.name_book = QLabel(self.price_frame)
        self.name_book.setObjectName(u"name_book")
        self.name_book.setStyleSheet(u"color:black;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color:none;\n"
"border:none;")

        self.horizontalLayout_3.addWidget(self.name_book)

        self.money_book = QLabel(self.price_frame)
        self.money_book.setObjectName(u"money_book")
        self.money_book.setEnabled(True)
        self.money_book.setStyleSheet(u"color:black;\n"
"font-size: 16pt;\n"
"background-color:none;\n"
"border:none;\n"
"margin-right:15px;\n"
"")
        self.money_book.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.money_book)

        self.per1pc_3 = QLabel(self.price_frame)
        self.per1pc_3.setObjectName(u"per1pc_3")
        self.per1pc_3.setStyleSheet(u"color:black;\n"
"font-size: 12pt;\n"
"background-color:none;\n"
"border:none;\n"
"margin-left:12px;")

        self.horizontalLayout_3.addWidget(self.per1pc_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.icon_magazine = QLabel(self.price_frame)
        self.icon_magazine.setObjectName(u"icon_magazine")
        self.icon_magazine.setMaximumSize(QSize(24, 16777215))
        self.icon_magazine.setStyleSheet(u"background-color:none;\n"
"border:none;")
        self.icon_magazine.setPixmap(QPixmap(u":/icon/icons/newspaper_FILL0_wght400_GRAD0_opsz24.svg"))

        self.horizontalLayout_2.addWidget(self.icon_magazine)

        self.name_magazine = QLabel(self.price_frame)
        self.name_magazine.setObjectName(u"name_magazine")
        self.name_magazine.setStyleSheet(u"color:black;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color:none;\n"
"border:none;")

        self.horizontalLayout_2.addWidget(self.name_magazine)

        self.money_magazine = QLabel(self.price_frame)
        self.money_magazine.setObjectName(u"money_magazine")
        self.money_magazine.setStyleSheet(u"color:black;\n"
"font-size: 16pt;\n"
"background-color:none;\n"
"border:none;\n"
"margin-right:15px;")
        self.money_magazine.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.money_magazine)

        self.per1pc_2 = QLabel(self.price_frame)
        self.per1pc_2.setObjectName(u"per1pc_2")
        self.per1pc_2.setStyleSheet(u"color:black;\n"
"font-size: 12pt;\n"
"background-color:none;\n"
"border:none;\n"
"margin-left:10px;")

        self.horizontalLayout_2.addWidget(self.per1pc_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icon_booklet = QLabel(self.price_frame)
        self.icon_booklet.setObjectName(u"icon_booklet")
        self.icon_booklet.setMaximumSize(QSize(24, 16777215))
        self.icon_booklet.setStyleSheet(u"background-color:none;\n"
"border:none;")
        self.icon_booklet.setPixmap(QPixmap(u":/icon/icons/relax_FILL0_wght400_GRAD0_opsz24.svg"))

        self.horizontalLayout.addWidget(self.icon_booklet)

        self.name_booklet = QLabel(self.price_frame)
        self.name_booklet.setObjectName(u"name_booklet")
        self.name_booklet.setStyleSheet(u"color:black;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color:none;\n"
"border:none;")

        self.horizontalLayout.addWidget(self.name_booklet)

        self.money_booklet = QLabel(self.price_frame)
        self.money_booklet.setObjectName(u"money_booklet")
        self.money_booklet.setStyleSheet(u"color:black;\n"
"font-size: 16pt;\n"
"background-color:none;\n"
"border:none;\n"
"margin-left:35px;")

        self.horizontalLayout.addWidget(self.money_booklet)

        self.per1pc = QLabel(self.price_frame)
        self.per1pc.setObjectName(u"per1pc")
        self.per1pc.setStyleSheet(u"color:black;\n"
"font-size: 12pt;\n"
"background-color:none;\n"
"border:none;\n"
"margin-left:12px;")

        self.horizontalLayout.addWidget(self.per1pc)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_5.addWidget(self.price_frame)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_new_trans = QPushButton(self.widget)
        self.btn_new_trans.setObjectName(u"btn_new_trans")
        self.btn_new_trans.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    background-color: rgba(255, 255, 255, 30);\n"
"    border: 1px solid rgba(255, 255, 255, 40);\n"
"    border-radius: 7px;\n"
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
        self.btn_new_trans.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.btn_new_trans)

        self.btn_adv = QPushButton(self.widget)
        self.btn_adv.setObjectName(u"btn_adv")
        self.btn_adv.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    background-color: rgba(255, 255, 255, 30);\n"
"    border: 1px solid rgba(255, 255, 255, 40);\n"
"    border-radius: 7px;\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/shopping_cart_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_adv.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.btn_adv)

        self.btn_edit = QPushButton(self.widget)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    background-color: rgba(255, 255, 255, 30);\n"
"    border: 1px solid rgba(255, 255, 255, 40);\n"
"    border-radius: 7px;\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/edit_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edit.setIcon(icon2)

        self.horizontalLayout_6.addWidget(self.btn_edit)

        self.btn_del = QPushButton(self.widget)
        self.btn_del.setObjectName(u"btn_del")
        self.btn_del.setStyleSheet(u"QPushButton {\n"
"    color: black;\n"
"    background-color: rgba(255, 255, 255, 30);\n"
"    border: 1px solid rgba(255, 255, 255, 40);\n"
"    border-radius: 7px;\n"
"    width: 180px;\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/delete_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_del.setIcon(icon3)

        self.horizontalLayout_6.addWidget(self.btn_del)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.tableView = QTableView(self.widget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"    background-color: rgba(255, 255, 255, 30);\n"
"    border: 1px solid rgba(255, 255, 255, 40);\n"
"    border-bottom-right-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgba(53, 53, 53);\n"
"    color: black;\n"
"    border: none;\n"
"    height: 50px;\n"
"    font-size: 14pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    border: none;\n"
"    color: white;\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(135)

        self.verticalLayout_3.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Publish App", None))
        self.txt.setText(QCoreApplication.translate("MainWindow", u"Total to pay", None))
        self.money_bal.setText(QCoreApplication.translate("MainWindow", u"$5000", None))
        self.txt_price.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.icon_own.setText("")
        self.name_own.setText(QCoreApplication.translate("MainWindow", u"Own edition", None))
        self.money_own.setText(QCoreApplication.translate("MainWindow", u"$100", None))
        self.per1pc_4.setText(QCoreApplication.translate("MainWindow", u"per 1 pc", None))
        self.txt_advertising.setText(QCoreApplication.translate("MainWindow", u"Advertising", None))
        self.icon_book.setText("")
        self.name_book.setText(QCoreApplication.translate("MainWindow", u"Books", None))
        self.money_book.setText(QCoreApplication.translate("MainWindow", u"$500", None))
        self.per1pc_3.setText(QCoreApplication.translate("MainWindow", u"per 1 pc", None))
        self.icon_magazine.setText("")
        self.name_magazine.setText(QCoreApplication.translate("MainWindow", u"Magazines", None))
        self.money_magazine.setText(QCoreApplication.translate("MainWindow", u"$300", None))
        self.per1pc_2.setText(QCoreApplication.translate("MainWindow", u"per 1 pc", None))
        self.icon_booklet.setText("")
        self.name_booklet.setText(QCoreApplication.translate("MainWindow", u"Booklets", None))
        self.money_booklet.setText(QCoreApplication.translate("MainWindow", u"$200", None))
        self.per1pc.setText(QCoreApplication.translate("MainWindow", u"per 1 pc", None))
        self.btn_new_trans.setText(QCoreApplication.translate("MainWindow", u"New transaction", None))
        self.btn_adv.setText(QCoreApplication.translate("MainWindow", u"Advertising", None))
        self.btn_edit.setText(QCoreApplication.translate("MainWindow", u"Edit transaction", None))
        self.btn_del.setText(QCoreApplication.translate("MainWindow", u"Delete transaction", None))
    # retranslateUi

