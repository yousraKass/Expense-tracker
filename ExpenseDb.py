import sqlite3
from datetime import date

class ExpenseDb:
    def __init__(self):
        self.conn = sqlite3.connect('Expenses.db')
        self.cur = self.conn.cursor()
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS Expenses
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                expense_name TEXT NOT NULL,
                price REAL NOT NULL,
                date DATE NULL)
            '''
        )

    def __del__(self):
        self.conn.close()

    def insert(self, expense, price, date):
        self.cur.execute(
            "INSERT INTO Expenses (expense_name, price, date) VALUES (?, ?, ?)",
            (expense, price, date)
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
        filtered_rows = [(expense_name, price, date) for _, expense_name, price, date in rows]
        return filtered_rows


    def get_paginated(self, offset, limit, target_year, target_month):
        """Fetch a limited number of expenses starting from an offset."""
        
        print("get paginated,", target_month, target_year)
        
        query = '''SELECT expense_name, price, date FROM Expenses WHERE date IS NOT NULL'''
        
        params = []
        
        if target_year is not None:
            query += " AND strftime('%Y', date) = ?"
            params.append(target_year)
        else:
            print("year null")
            
        if target_month is not None:
            if len(target_month) == 1 :
                target_month = "0" + target_month

            query += " AND strftime('%m', date) = ?"
            params.append(target_month)
        else:
            print("month null")
            
        query += " LIMIT ? OFFSET ?"
        params.extend([limit, offset])
        
        self.cur.execute(query, tuple(params))
        result = self.cur.fetchall()
        return result

    def count_expenses(self):
        """Count total number of expenses."""
        self.cur.execute("SELECT COUNT(*) FROM Expenses")
        return self.cur.fetchone()[0]
    
    def fetch_with_date(self, target_date):
        self.cur.execute('SELECT * FROM Expenses WHERE date = ?', (target_date,))
        results = self.cur.fetchall()
        
        return results

