import sys
from PyQt5.QtWidgets import QApplication


from ExpenseApp import ExpenseApp


app = QApplication(sys.argv)
window = ExpenseApp()
window.show()
sys.exit(app.exec_())