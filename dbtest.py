from ExpenseDb import ExpenseDb

db = ExpenseDb()
db.insert('hehe', 10)
print(db.getAll())