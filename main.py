import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlTableModel
from ui_main import Ui_MainWindow
from new_transaction import Ui_Dialog
from connection import Data



class PublishApp(QMainWindow):
    def __init__(self, db_name):
        super(PublishApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data(db_name)
        self.view_data()
        self.reload_data()

        self.ui.btn_new_trans.clicked.connect(self.open_new_transaction_window)
        self.ui.btn_edit.clicked.connect(self.open_new_transaction_window)
        self.ui.btn_del.clicked.connect(self.delete_current_transaction)

        self.ui.tableView.setColumnWidth(0, 100)
        self.ui.tableView.setColumnWidth(1, 110)
        self.ui.tableView.setColumnWidth(2, 110)
        self.ui.tableView.setColumnWidth(3, 100)
        self.ui.tableView.setColumnWidth(4, 100)
        self.ui.tableView.setColumnWidth(5, 100)
        self.ui.tableView.setStyleSheet("QTableView::item { padding: 5px; }")

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('test1')
        self.model.select()
        self.ui.tableView.setModel(self.model)
        self.reload_data()
        self.ui.tableView.verticalHeader().setVisible(False)  # Приховати вертикальну шапку (номери рядків)



    def reload_data(self):
        self.ui.money_bal.setText(self.conn.total_balance())

    def open_new_transaction_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()
        if sender.text() == "New transaction":
            self.ui_window.button_Nt.clicked.connect(self.add_new_transaction)
        else:
            self.ui_window.button_Nt.clicked.connect(self.edit_current_transaction)


    def add_new_transaction(self):
        modell = self.ui_window.choose_cat_Nt.currentText()
        name = self.ui_window.name_Nt.text()
        adv = self.ui_window.adv_Nt.currentText()
        amount = self.ui_window.amount_Nt.text()
        costs = 100
        contacts = self.ui_window.contacts_Nt.text()

        self.conn.add_new_transaction_query(modell, name, adv, amount, costs, contacts)

        self.reload_data()
        self.view_data()
        self.new_window.close()

    def edit_current_transaction(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))

        modell = self.ui_window.choose_cat_Nt.currentText()
        name = self.ui_window.name_Nt.text()
        adv = self.ui_window.adv_Nt.currentText()
        amount = self.ui_window.amount_Nt.text()
        costs = 100
        contacts = self.ui_window.contacts_Nt.text()

        self.conn.update_transaction_query(modell, name, adv, amount, costs, contacts, id)
        self.reload_data()
        self.view_data()
        self.new_window.close()

    def delete_current_transaction(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))

        self.conn.delete_transaction_query(id)

        self.reload_data()
        self.view_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PublishApp("publish_db.db")
    window.show()

    sys.exit(app.exec())