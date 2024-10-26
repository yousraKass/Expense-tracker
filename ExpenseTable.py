from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from ExpenseDb import ExpenseDb


class ExpenseTable(QTableWidget):
    def __init__(self):
        super().__init__(0, 2)
        self.db = ExpenseDb()
        self.setHorizontalHeaderLabels(["Expense", "Price"])
        self.populate_initial_data()

    def populate_initial_data(self):
        #initial_data = [("Veg", 40.0), ("Fruit", 70.0), ("Fuel", 60.0)]
        initial_data = self.db.getAll()
        print(self.db.getAll())
        self.setRowCount(len(initial_data))
        for row, (expense, price) in enumerate(initial_data):
            self.setItem(row, 0, QTableWidgetItem(expense))
            self.setItem(row, 1, QTableWidgetItem(str(price)))

    def add_expense(self, expense_name, price_text):
        row_position = self.rowCount()
        self.db.insert(expense_name, price_text)
        self.insertRow(row_position)
        self.setItem(row_position, 0, QTableWidgetItem(expense_name))
        self.setItem(row_position, 1, QTableWidgetItem(price_text))

    # Delete expense ( we should click on the entire row from its number to delete it )
    # def delete_expense(self):
    #     selected_rows = self.selectionModel().selectedRows()
    #     for index in sorted(selected_rows, reverse=True):
    #         self.removeRow(index.row())
    #

    def delete_expense(self):
        selected_rows = self.selectionModel().selectedRows()
        for index in sorted(selected_rows, reverse=True):
            # Get the expense name from the first column of the selected row
            expense_item = self.item(index.row(), 0)  # Column 0 is for expense names
            if expense_item is not None:  # Check if the item exists
                expense_name = expense_item.text()  # Get the text of the item

                # Call the database delete method with the expense name
                self.db.delete(expense_name)

            # Remove the row from the table
            self.removeRow(index.row())
