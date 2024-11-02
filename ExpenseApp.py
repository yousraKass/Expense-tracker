from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QFrame, QComboBox,
    QLineEdit, QLabel, QPushButton
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

        self.filter_container = QFrame()
        filter_layout = QVBoxLayout()
        
        year_label = QLabel()
        year_label.setText("Enter year")
        
        
        month_label = QLabel()
        month_label.setText("Enter Month")
        
        year_input = QLineEdit()
        year_input.setPlaceholderText("enter the year here")
        
        month_input = QLineEdit()
        month_input.setPlaceholderText("enter month here")
        
        btn = QPushButton("show")
        btn2 = QPushButton("download")

        
        
        
        filter_layout.addWidget(year_label)
        filter_layout.addWidget(year_input)
        filter_layout.addWidget(month_label)
        filter_layout.addWidget(month_input)
        filter_layout.addWidget(btn)
        filter_layout.addWidget(btn2)


        
        self.filter_container.setLayout(filter_layout)
        
        layout.addWidget(self.filter_container)
        
        
        # Expense table
        self.table = ExpenseTable()  # Create the table instance
        layout.addWidget(self.table)
        pagination_controls = self.table.create_pagination_controls()
        layout.addWidget(pagination_controls)

        # Input section, pass the ExpenseTable instance
        self.input_section = InputSection(self.add_expense, self.table)
        layout.addWidget(self.input_section)

        # Total display
        self.total_display = TotalDisplay()
        layout.addWidget(self.total_display)

        self.update_total()
        total_exp = self.update_total()
       


        # export pdf from function export_to_pdf in ExpenseTable
        btn2.clicked.connect(lambda: self.table.export_to_pdf(year_input.text(), month_input.text(), total_exp))
        layout.addWidget(btn2)

        

        
    def add_expense(self):
        # Get the inputs from the input section
        expense_name, price_text = self.input_section.get_inputs()
        # Add the expense to the table
        self.table.add_expense(expense_name, price_text)
        # Clear the inputs after adding the expense
        self.input_section.clear_inputs()
        # Update the total after adding the expense
        self.update_total()

    def update_total(self):
        total = 0.0
        # Iterate through the rows in the table to calculate the total
        for row in range(self.table.rowCount()):
            price_item = self.table.item(row, 1)
            if price_item:
                try:
                    total += float(price_item.text())
                except ValueError:
                    pass  # Ignore items that cannot be converted to float
              
        # Update the total display
        self.total_display.update_total(total)
        return total

        
