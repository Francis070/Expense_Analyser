from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('expense.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.html')
    conn = get_db_connection()
    posts = conn.execute('''SELECT datetime, txn_id, source, txn_type, amount, sub_source, category, sub_category, 
    spent_desc, wasted FROM transactions''').fetchall()
    conn.close()
    return render_template('home.html', rows = rows)
    # try:
    #     if request.method == 'POST':
    #
    #         # use = session['user'].get("name")
    #         # ema = session['user'].get("preferred_username")
    #
    #         conn = sqlite3.connect('expense.db')
    #         c = conn.cursor()
    #         c.execute('''SELECT * FROM transactions''')
    #
    #         rows = c.fetchall()
    #         print('try is running')
    #         return render_template("home.html", rows=rows)
    # except:
    #     # for row in rows:
    #     #     print(row)
    #     #
    #     # conn.close()
    #     print('except is running')
    #     return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)