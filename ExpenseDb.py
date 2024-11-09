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
            "INSERT INTO Expenses (expense_name, price) VALUES (?, ?)",
            (expense, price)
        )
        self.conn.commit()

    def delete(self, expense):
        self.cur.execute(
            "DELETE FROM Expenses WHERE expense_name = ?",
            (expense,)
        )
        self.conn.commit()

    def getAll(self):
        self.cur.execute("SELECT * FROM Expenses")
        rows = self.cur.fetchall()
        filtered_rows = [(expense_name, price) for _, expense_name, price in rows]
        return filtered_rows


    def get_paginated(self, offset, limit):
        """Fetch a limited number of expenses starting from an offset."""
        self.cur.execute("SELECT expense_name, price FROM Expenses LIMIT ? OFFSET ?", (limit, offset))
        return self.cur.fetchall()

    def count_expenses(self):
        """Count total number of expenses."""
        self.cur.execute("SELECT COUNT(*) FROM Expenses")
        return self.cur.fetchone()[0]
