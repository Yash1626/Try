from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS balance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS budget (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS income (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expense (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT INTO balance (amount) VALUES (0)
    ''')
    cursor.execute('''
        INSERT INTO budget (amount) VALUES (0)
    ''')
    conn.commit()
    conn.close()

@app.route('/deposit', methods=['POST'])
def deposit():
    data = request.get_json()
    amount = data['amount']
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE balance SET amount = amount + ?', (amount,))
    cursor.execute('INSERT INTO income (amount) VALUES (?)', (amount,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

@app.route('/spend', methods=['POST'])
def spend():
    data = request.get_json()
    amount = data['amount']
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE balance SET amount = amount - ?', (amount,))
    cursor.execute('UPDATE budget SET amount = amount - ?', (amount,))
    cursor.execute('INSERT INTO expense (amount) VALUES (?)', (amount,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

@app.route('/set_budget', methods=['POST'])
def set_budget():
    data = request.get_json()
    amount = data['amount']
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE budget SET amount = ?', (amount,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

@app.route('/get_budget', methods=['GET'])
def get_budget():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('SELECT amount FROM budget')
    budget = cursor.fetchone()[0]
    conn.close()
    return jsonify({'budget': budget, 'budget_set': budget > 0})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
