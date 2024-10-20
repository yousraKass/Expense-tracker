from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem 
    

class ExpenseTable(QTableWidget):
    def __init__(self):
        super().__init__(0, 2)
        self.setHorizontalHeaderLabels(["Expense", "Price"])
        self.populate_initial_data()

    def populate_initial_data(self):
        initial_data = [("Veg", 40.0), ("Fruit", 70.0), ("Fuel", 60.0)]
        self.setRowCount(len(initial_data))
        for row, (expense, price) in enumerate(initial_data):
            self.setItem(row, 0, QTableWidgetItem(expense))
            self.setItem(row, 1, QTableWidgetItem(str(price)))

    def add_expense(self, expense_name, price_text):
        row_position = self.rowCount()
        self.insertRow(row_position)
        self.setItem(row_position, 0, QTableWidgetItem(expense_name))
        self.setItem(row_position, 1, QTableWidgetItem(price_text))

    # Delete expense
    def delete_expense(self):
        selected_rows = self.selectionModel().selectedRows()
        for index in sorted(selected_rows, reverse=True):
            self.removeRow(index.row()) 
    