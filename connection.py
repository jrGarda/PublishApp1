from PySide6 import QtWidgets, QtSql


class Data:
    def __init__(self, db_name):  # Додайте аргумент db_name
        super(Data, self).__init__()
        self.db_name = db_name  # Збережіть назву бази даних
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(self.db_name)  # Використовуйте збережену назву

        if not db.open():
            QtWidgets.QMessageBox.critical(None,"Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS test1 (ID integer primary key AUTOINCREMENT ,"
                   "Type VARCHAR(20),Name VARCHAR(20), ADV VARCHAR(10), Amount integer, Costs integer, Contacts VARCHAR(20))")
        return True


    def execute_query_with_params(self, sql_query, query_values = None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()
        return query

    def add_new_transaction_query(self, modell, name, adv, amount, costs, contacts):
        sql_query = "INSERT INTO test1 (Type, Name, ADV, Amount, Costs, Contacts) VALUES (?, ?, ?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [modell, name, adv, amount, costs, contacts])

    def update_transaction_query(self, modell, name, adv, amount, costs, contacts, id):
        sql_query = "UPDATE test1 SET Type=?, Name=?, ADV=?, Amount=?, Costs=?, Contacts=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [modell, name, adv, amount, costs, contacts, id])



    def delete_transaction_query(self, id):
        sql_query = "DELETE FROM test1 WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

    def get_total(self, column, multiplier_column=None, filter=None, value=None):
        sql_query = f"SELECT SUM({column} * {multiplier_column}) FROM test1"

        if filter is not None and value is not None:
            sql_query += f" WHERE {filter} = ?"

        query_values = []

        if value is not None:
            query_values.append(value)

        query = self.execute_query_with_params(sql_query, query_values)

        if query.next():
            return str(query.value(0)) + '$'

        return '0'

    def total_balance(self):
        return self.get_total(column="Costs", multiplier_column="Amount")
