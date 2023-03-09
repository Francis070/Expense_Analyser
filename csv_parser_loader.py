import pandas as pd
import sqlite3

# data = pd.read_csv(r'C:\Users\amiab\Projects\Expense Manager\csv_files\Category.csv')
data = pd.read_csv(r'C:\Users\amiab\Projects\Expense Manager\csv_files\Source.csv')
df = pd.DataFrame(data)

conn = sqlite3.connect('expense.db')
print('opened DB successfully')

# Category

# for row in range(len(df)):
#     category_id = df.iloc[row]['category_id']
#     category = df.iloc[row]['category']
#     sub_category = df.iloc[row]['sub_category']
#     planned_budget = df.iloc[row]['planned_budget']
#
#     params = (category_id, category, sub_category, planned_budget)
#     insert_val = '''insert into category values(?, ?, ?, ?);'''
#     conn.execute(insert_val, params)

# Source

for row in range(len(df)):
    source_id = df.iloc[row]['source_id']
    source = df.iloc[row]['source']
    sub_source = df.iloc[row]['sub_source']

    params = (source_id, source, sub_source)
    insert_val = '''insert into source values(?, ?, ?);'''
    conn.execute(insert_val, params)


conn.commit()
conn.close()
