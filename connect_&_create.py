import sqlite3

conn = sqlite3.connect('expense.db')

print('opened DB successfully')

####----untracked_transaction----

# conn.execute('drop table if exists untracked_txn;')
#
# conn.execute('''create table if not exists untracked_txn (
# datetime varchar(50),
# amount varchar(50),
# txn_id varchar(100),
# txn_desc varchar(200),
# txn_type varchar(100),
# source varchar(100),
# balance varchar(50)
# );''')

####----transaction----

# conn.execute('drop table if exists transactions;')
#
# conn.execute('''create table if not exists transactions (
# expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
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


####----Category----

# conn.execute('drop table if exists category;')
#
# conn.execute('''create table if not exists category (
# category_id varchar(100),
# category varchar(100),
# sub_category varchar(200),
# planned_budget real
# );''')

####----Source----

conn.execute('drop table if exists source;')

conn.execute('''create table if not exists source (
source_id varchar(200),
source varchar(200),
sub_source varchar(200)
);''')

print("Table created successfully")

conn.commit()
conn.close()