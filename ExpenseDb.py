import sqlite3
from datetime import date, datetime

class ExpenseDb:
    def __init__(self):
        self.conn = sqlite3.connect('Expenses.db')
        self.cur = self.conn.cursor()
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS Expenses
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                expense_name TEXT NOT NULL,
                price REAL NOT NULL,
                date TEXT
                )''')

    def __del__(self):
        self.conn.close()


    def insert(self, expense, price):
        dateOfInsertion = datetime.today()
        dateOfInsertion = datetime.strftime(dateOfInsertion, "%Y-%m-%d")
        self.cur.execute(
            "insert into Expenses (expense_name, price, date) values (?,?,?)",
            (expense, price, dateOfInsertion)
        )
        self.conn.commit()


    def delete(self, expense):
        self.cur.execute(
            "delete from Expenses where expense_name=?",
            (expense,)
        )
        self.conn.commit()

    def getAll(self, month = -1, year = -1):
        self.cur.execute(
            "select * from Expenses"
        )
        rows = self.cur.fetchall()
        selected_rows = []
        if month != -1 and year == -1 and month >= 0 and month <= 12:
            for row in rows:
                if int(row[3][5:7]) == int(month):
                    selected_rows.append(row)
                    print(row)

        elif year != -1 and month == -1:
            for row in rows:
                if int(row[3][0:4]) == int(year):
                    selected_rows.append(row)
                    print(row)

        elif year != -1 and  month != -1 and month >= 0 and month <= 12:
            for row in rows:
                if int(row[3][0:4]) == int(year) and int(row[3][5:7]) == int(month):
                    selected_rows.append(row)
                    print(row)
                    print("hehe")


        elif month == -1 and year == -1:
            selected_rows = rows

        filtered_rows = [(expense_name, price) for _, expense_name, price, datee in selected_rows]
        return filtered_rows