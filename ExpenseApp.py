from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout
)

from MenuBar import MenuBar
from InputSection import InputSection
from ExpenseTable import ExpenseTable
from TotalDisplay import TotalDisplay


class ExpenseApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Expense Tracker")
        self.setGeometry(100, 100, 600, 300)
        self.setup_ui()

    def setup_ui(self):
        # Central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Menu bar
        self.menu_bar = MenuBar(self)
        self.setMenuBar(self.menu_bar)

        # Input section
        self.input_section = InputSection(self.add_expense)
        layout.addWidget(self.input_section)

        # Expense table
        self.table = ExpenseTable()
        layout.addWidget(self.table)

        # Total display
        self.total_display = TotalDisplay()
        layout.addWidget(self.total_display)

        # Update total 
        self.update_total()

    def add_expense(self):
        expense_name, price_text = self.input_section.get_inputs()
        self.table.add_expense(expense_name, price_text)
        self.input_section.clear_inputs()
        self.update_total()

    def update_total(self):
        total = 0.0
        for row in range(self.table.rowCount()):
            price_item = self.table.item(row, 1)
            if price_item:
                total += float(price_item.text())
        self.total_display.update_total(total)
