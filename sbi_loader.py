import pandas as pd
# import sqlite3
import psycopg2

# conn = sqlite3.connect('expense.db')
dbname = "postgres"
user = "postgres"
password = "Postgresql"
host = "localhost"
port = "5432"

conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)
cur = conn.cursor()
source = 'SBI'

path = r'C:\Users\amiab\Projects\Expense Manager\bank_statement\SBI\1674916118250LUS5WmVN15QZ9SD9.csv'

df = pd.DataFrame(pd.read_csv(path))
header = [x.strip() for x in df.columns]
df.columns = header

# print(df.head())

for row in range(len(df)):
    datetime = df.iloc[row]['Txn Date']
    txn_desc = df.iloc[row]['Description']
    balance = df.iloc[row]['Balance']
    txn_id = df.iloc[row]['Ref No./Cheque No.']
    if not isinstance(txn_id, float):
        txn_id = txn_id.strip()
        txn_id = df.iloc[row]['Ref No./Cheque No.'].split()[-1]
    else:
        txn_id = ''
    amount = 0
    txn_type = ''
    # print(df.iloc[row]['Debit'])

    if df.iloc[row]['Debit'].strip() == '':
        amount = df.iloc[row]['Credit']
        txn_type += 'Credit'
    else:
        amount = df.iloc[row]['Debit']
        txn_type += 'Debit'

    params = (datetime, amount, txn_id, txn_desc, txn_type, source, balance)

    insert_val = '''insert into untracked_txn values(%s, %s, %s, %s, %s, %s, %s);'''

    cur.execute(insert_val, params)

cur.close()
conn.commit()
conn.close()





