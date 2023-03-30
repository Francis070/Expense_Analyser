from flask import Flask, request, jsonify, render_template
import sqlite3


HOST_NAME = '127.0.0.1'
HOST_PORT = 5000
DBFILE = 'expense.db'

app = Flask(__name__)

def get_txn_data():
    conn = sqlite3.connect(DBFILE)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM 'transactions' where sub_source is null and category is null and sub_category 
    is null and spent_desc is null''')
    results = cursor.fetchall()
    conn.close()
    return results

def get_src_data():
    conn = sqlite3.connect(DBFILE)
    cursor = conn.cursor()
    cursor.execute(''' SELECT distinct sub_source FROM 'source' ''')
    results = cursor.fetchall()
    res = [x[0] for x in results]
    conn.close()
    return res

def get_cat_data():
    conn = sqlite3.connect(DBFILE)
    cursor = conn.cursor()
    cursor.execute(''' SELECT distinct category FROM 'category' ''')
    results = cursor.fetchall()
    res = [x[0] for x in results]
    conn.close()
    return res

def get_subcat_data():
    conn = sqlite3.connect(DBFILE)
    cursor = conn.cursor()
    cursor.execute(''' SELECT distinct sub_category FROM 'category' ''')
    results = cursor.fetchall()
    res = [x[0] for x in results]
    conn.close()
    return res

@app.route("/")
def home():
    txn_data = get_txn_data()
    src_data = get_src_data()
    cat_data = get_cat_data()
    sub_cat_data = get_subcat_data()
    return render_template("home.html", txn=txn_data, src=src_data, cat=cat_data, subcat=sub_cat_data)

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        # Get input from user and update data in database
        id = request.form.getlist('id')
        sub_source = request.form.getlist('sub_source')
        category = request.form.getlist('category')
        sub_category = request.form.getlist('sub_category')
        spent_desc = request.form.getlist('spent_desc')
        wasted = request.form.getlist('wasted')

        for i in range(len(id)):
            waste = False
            if wasted[i] == 'Yes':
                waste = True
            conn = sqlite3.connect(DBFILE)
            cursor = conn.cursor()
            cursor.execute('''UPDATE 'transactions' SET sub_source = ?,  category = ?,
            sub_category = ?, spent_desc = ?, wasted = ?
            WHERE txn_id = ? ''', (sub_source[i], category[i], sub_category[i], spent_desc[i], waste, id[i]))
            # print(
            #     id[i] + ' ' + sub_source[i] + ' ' + category[i] + ' ' + sub_category[i] + ' ' + spent_desc[i] + ' ' + str(waste))

        conn.commit()
        conn.close()

        txn_data = get_txn_data()
        src_data = get_src_data()
        cat_data = get_cat_data()
        sub_cat_data = get_subcat_data()
        return render_template("home.html", txn=txn_data, src=src_data, cat=cat_data, subcat=sub_cat_data)

if __name__ == "__main__":
    app.run(HOST_NAME, HOST_PORT)