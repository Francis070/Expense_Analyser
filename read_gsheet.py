import pandas as pd

sheet_url = "https://docs.google.com/spreadsheets/d/1Gf7xdWMNx2mgmlDTPuZZ-QX287qbLVA8XTbb7dXLPc8/edit#gid=0"
url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')

df = pd.read_csv(url)

for column in df.columns:
    print(df[column])
