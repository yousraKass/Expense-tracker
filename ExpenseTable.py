from PyQt5.QtWidgets import (
    QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout, QWidget
)
from ExpenseDb import ExpenseDb

class ExpenseTable(QTableWidget):
    def __init__(self, items_per_page=10):
        super().__init__(0, 2)
        self.db = ExpenseDb()
        self.items_per_page = items_per_page
        self.current_page = 0
        self.setHorizontalHeaderLabels(["Expense", "Price"])
        self.populate_page()


    def populate_page(self):
        # Clear current rows
        self.setRowCount(0)
        
        # Retrieve expenses for the current page from the database
        offset = self.current_page * self.items_per_page
        expenses = self.db.get_paginated(offset, self.items_per_page)  # Use get_paginated here
        
        # Populate table with paginated data
        for row, (expense, price) in enumerate(expenses):
            self.insertRow(row)
            self.setItem(row, 0, QTableWidgetItem(expense))
            self.setItem(row, 1, QTableWidgetItem(str(price)))


    def add_expense(self, expense_name, price_text):
        # Insert the new expense into the database
        self.db.insert(expense_name, price_text)
        
        # Refresh current page to reflect any additions
        self.populate_page()

    def delete_expense(self):
        selected_rows = self.selectionModel().selectedRows()
        for index in sorted(selected_rows, reverse=True):
            expense_item = self.item(index.row(), 0)
            if expense_item:
                expense_name = expense_item.text()
                self.db.delete(expense_name)
            self.removeRow(index.row())
        self.populate_page()

    def next_page(self):
        # Go to the next page if there is data
        total_expenses = self.db.count_expenses()
        if (self.current_page + 1) * self.items_per_page < total_expenses:
            self.current_page += 1
            self.populate_page()

    def previous_page(self):
        # Go to the previous page if we are not on the first page
        if self.current_page > 0:
            self.current_page -= 1
            self.populate_page()

    def create_pagination_controls(self):
        # Pagination controls layout
        controls_layout = QHBoxLayout()
        
        # Previous button
        prev_button = QPushButton("Previous")
        prev_button.clicked.connect(self.previous_page)
        controls_layout.addWidget(prev_button)
        
        # Next button
        next_button = QPushButton("Next")
        next_button.clicked.connect(self.next_page)
        controls_layout.addWidget(next_button)
        
        # Return the layout to be added in the main UI
        controls_widget = QWidget()
        controls_widget.setLayout(controls_layout)
        return controls_widget
