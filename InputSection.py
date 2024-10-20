from PyQt5.QtWidgets import ( 
    QLineEdit, QLabel, QPushButton, QWidget, QHBoxLayout
)
from ExpenseTable import ExpenseTable

class InputSection(QWidget):
    def __init__(self, add_expense_callback, expense_table):
        super().__init__()
        self.expense_table = expense_table 
        self.expense_input = QLineEdit()
        self.price_input = QLineEdit()
        self.setup_input_layout(add_expense_callback)

    def setup_input_layout(self, add_expense_callback):
        layout = QHBoxLayout(self)

        # Labels and input fields
        expense_label = QLabel("Expense:")
        self.expense_input.setFixedWidth(150)
        price_label = QLabel("Price:")
        self.price_input.setFixedWidth(100)

        # Add button
        add_button = QPushButton("Add Expense")
        add_button.clicked.connect(add_expense_callback)

        # Create the button to delete selected expenses
        delete_button = QPushButton("Delete Expense")
        delete_button.clicked.connect(self.expense_table.delete_expense) 

        # Add widgets to layout
        layout.addWidget(expense_label)
        layout.addWidget(self.expense_input)
        layout.addWidget(price_label)
        layout.addWidget(self.price_input)
        layout.addWidget(add_button)
        layout.addWidget(delete_button)

    def get_inputs(self):
        return self.expense_input.text().strip(), self.price_input.text().strip()

    def clear_inputs(self):
        self.expense_input.clear()
        self.price_input.clear()
