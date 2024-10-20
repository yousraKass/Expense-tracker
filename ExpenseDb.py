import sqlite3

class ExpenseDb:
    def __init__(self):
        self.conn = sqlite3.connect('Expenses.db')
        self.cur = self.conn.cursor()
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS Expenses
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                expense_name TEXT NOT NULL,
                price REAL NOT NULL)''')

    def __del__(self):
        self.conn.close()


    def insert(self, expense, price):
        self.cur.execute(
            "insert into Expenses (expense_name, price) values (?,?)",
            (expense, price)
        )
        self.conn.commit()


    def delete(self, expense):
        self.cur.execute(
            "delete from Expenses where expense_name=?",
            (expense,)
        )
        self.conn.commit()

    def getAll(self):
        self.cur.execute(
            "select * from Expenses"
        )
        rows = self.cur.fetchall()
        return rows