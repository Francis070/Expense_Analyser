import sqlite3

conn = sqlite3.connect('expense.db')

print('opened DB successfully')

conn.execute('drop table if exists untracked_txn;')

conn.execute('''create table if not exists untracked_txn (
datetime varchar(50),
amount real,
txn_id varchar(100),
txn_desc varchar(200),
txn_type varchar(100),
source varchar(100),
balance real
);''')


# conn.execute('drop table if exists transactions ;')
#
# conn.execute('''create table if not exists transactions (
# datetime date,
# amount real,
# txn_id varchar(100),
# txn_desc varchar(200),
# txn_type varchar(100),
# balance real,
# source varchar(100),
# sub_source varchar(200),
# category varchar(100),
# sub_category varchar(200),
# spent_desc varchar(300),
# wasted boolean
# );''')

print("Table created successfully")

conn.commit()
conn.close()