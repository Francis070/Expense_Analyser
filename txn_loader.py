import sqlite3

conn = sqlite3.connect('expense.db')

print('Opened transaction table successfully')

conn.execute('truncate table if exists untracked_txn;')

conn.execute(
'''insert into transactions 
select
case 
when substr(datetime, 4, 3) = 'Jan' then date('20'||substr(datetime,8,2)||'-01-'||substr(datetime,1,2))
when substr(datetime, 4, 3) = 'Feb' then date('20'||substr(datetime,8,2)||'-02-'||substr(datetime,1,2))
when substr(datetime, 4, 3) = 'Mar' then date('20'||substr(datetime,8,2)||'-03-'||substr(datetime,1,2))
when substr(datetime, 4, 3) = 'Apr' then date('20'||substr(datetime,8,2)||'-04-'||substr(datetime,1,2))
when substr(datetime, 4, 3) = 'May' then date('20'||substr(datetime,8,2)||'-05-'||substr(datetime,1,2))
when substr(datetime, 4, 3) = 'Jun' then date('20'||substr(datetime,8,2)||'-06-'||substr(datetime,1,2))
when substr(datetime, 4, 3) = 'Jul' then date('20'||substr(datetime,8,2)||'-07-'||substr(datetime,1,2))
when substr(datetime, 4, 3) = 'Aug' then date('20'||substr(datetime,8,2)||'-08-'||substr(datetime,1,2))
when substr(datetime, 4, 3) = 'Sep' then date('20'||substr(datetime,8,2)||'-09-'||substr(datetime,1,2))
when substr(datetime, 4, 3) = 'Oct' then date('20'||substr(datetime,8,2)||'-10-'||substr(datetime,1,2))
when substr(datetime, 4, 3) = 'Nov' then date('20'||substr(datetime,8,2)||'-11-'||substr(datetime,1,2))
when substr(datetime, 4, 3) = 'Dec' then date('20'||substr(datetime,8,2)||'-12-'||substr(datetime,1,2))
end as datetime,
CAST(replace(amount, ',', '') as decimal) as amount,
txn_id as txn_id,
txn_desc as txn_desc,
txn_type as txn_type,
CAST(replace(balance, ',', '') as decimal) as balance,
source as source,
null as sub_source,
null as category,
null as sub_category,
null as spent_desc,
false as wasted
from untracked_txn;''')

print("Inserted data successfully")

conn.commit()
conn.close()