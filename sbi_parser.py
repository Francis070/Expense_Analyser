import pandas as pd
import os


dir = r'C:\Users\amiab\Projects\Expense Manager\bank_statement\SBI'

def convert_csv(file_name):
    checker = False
    file, ext = file_name.split('.')
    inputFile = open(file_name, "r")
    exportFile = open('op.' + ext, "w")
    for line in inputFile:

        if line.startswith('Txn Date'):
            checker = True

        if checker:
            if not line.startswith('**'):
                exportFile.write(line.rstrip('\t'))

    inputFile.close()
    exportFile.close()
    os.remove(file_name)
    os.rename('op.txt', file_name)

os.chdir(dir)

for x in os.listdir():
    if x.endswith(".xls"):
        file_name = os.path.splitext(x)[0]
        os.rename(x, file_name + '.txt')

for x in os.listdir():
    if x.endswith(".txt"):
        convert_csv(x)
        file_name = os.path.splitext(x)[0]
        df = pd.read_csv(dir + '\\' + file_name + '.txt', sep='\t', header=None)
        df.to_csv(dir + '\\' + file_name + '.csv', header=False, index=False)
        os.remove(dir + '\\' + file_name + '.txt')




