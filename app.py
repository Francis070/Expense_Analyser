from flask import Flask, request, jsonify, render_template
import sqlite3


HOST_NAME = '127.0.0.1'
HOST_PORT = 5000
DBFILE = 'expense.db'

app = Flask(__name__)

def get_db_data():
    conn = sqlite3.connect(DBFILE)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM 'transactions' where sub_source is null and category is null and sub_category 
    is null and spent_desc is null''')
    results = cursor.fetchall()
    conn.close()
    return results


@app.route("/")
def home():
    data = get_db_data()
    # print(users)

    # (C2) RENDER HTML PAGE
    return render_template("home.html", dt=data)

if __name__ == "__main__":
    app.run(HOST_NAME, HOST_PORT)