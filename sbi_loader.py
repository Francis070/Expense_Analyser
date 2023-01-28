import pandas as pd

source = 'SBI'

path = r'C:\Users\amiab\Projects\Expense Manager\bank_statement\SBI\1674916118250LUS5WmVN15QZ9SD9.csv'

df = pd.read_csv(path)
# print(df.head())
print(df.loc[0, :])
# for line in range(len(df)):
#     print(df.loc[[line]])