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

print('opened DB successfully')

####----untracked_transaction----
cur = conn.cursor()

# cur.execute('drop table if exists public.untracked_txn;')
#
# cur.execute('''create table if not exists public.untracked_txn (
# datetime varchar(50),
# amount varchar(50),
# txn_id varchar(100),
# txn_desc varchar(200),
# txn_type varchar(100),
# source varchar(100),
# balance varchar(50)
# );''')

####----transaction----

# cur.execute('drop table if exists transactions;')
#
# cur.execute('''create table if not exists transactions (
# expense_id SERIAL PRIMARY KEY ,
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

# cur.execute('drop table if exists category;')
#
# cur.execute('''create table if not exists category (
# category_id varchar(100),
# category varchar(100),
# sub_category varchar(200),
# planned_budget real
# );''')

####----Source----

cur.execute('drop table if exists source;')

cur.execute('''create table if not exists source (
source_id varchar(200),
source varchar(200),
sub_source varchar(200)
);''')

print("Table created successfully")

# cur.commit()
cur.close()
conn.commit()
conn.close()