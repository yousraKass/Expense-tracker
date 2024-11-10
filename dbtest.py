from ExpenseDb import ExpenseDb
from datetime import date

db = ExpenseDb()

my_date = date(year=2023, day=20, month=5)
db.insert('HEHEHE', 10, my_date)
print(db.getAll())