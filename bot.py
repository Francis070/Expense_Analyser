import telebot
from datetime import datetime
import requests
import re


# ----------If the script generates connection timed out error then uncomment the
# ------------------------below line and execute the whole program
# requests.get('https://google.com', verify=False)

token = ''
with open('token.txt', 'r') as f:
    token = f.read()

bot = telebot.TeleBot(token)
def expense_report(text):
    txn_keyword = ['SBI', 'Transaction', 'from', 'to', 'Paid', 'Paytm', 'Food Wallet', 'Rs', 'A/c',
                   'debited', 'credited', 'Ref', 'Ref No', 'transfer to', 'UPI', 'Txn ID', 'payment',
                   'successfully', 'succeeded', 'Union Bank of India', 'Union Bank', 'SBI Debit Card',
                   'NEFT', 'UTR', 'PhonePe', 'Google Pay', 'Gpay', 'debit', 'credit', 'cash', 'IFSC',
                   'IMPS', 'Payment Gateway', 'failed']

    #---Not a expense receipt.

    if not (any(x.lower() in text.lower() for x in txn_keyword)):
        return "This is not a transaction message."

    #---For Cash
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M")

    if 'cash' in text.lower():
        type = 'Debit'
        if type.lower() not in text.lower():
            type = 'Credit'

        amount = re.findall(r'[0-9]+', text)
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M")
        report = '''Datetime : {}
Amount : {}
Transaction ID : N/A
Type : {}
Source : Wallet
Mode : Cash'''.format(dt_string, amount[0], type)

        print(report)
        return report

    #----transaction type

    # debit = ['paid', 'debited']
    credit = ['added', 'credited', 'received']
    txn_type = ''

    if any(x.lower() in text.lower() for x in credit):
        txn_type += 'Credit'
    else:
        txn_type += 'Debit'

    #----Amount

    re_amt = re.compile(r'(?:Rs\.?|INR)\s*(\d+(?:[.,]\d+)*)|(\d+(?:[.,]\d+)*)\s*(?:Rs\.?|INR)')
    # txn_amt = re.findall('Rs.?[0-9+]]', text)
    txn_amt = re_amt.findall(text)
    # report = txn_type + ' ' + txn_amt[0]
    txn_amt = txn_amt[0][0]
    # print(txn_amt)

    #---- Reference number
    txn_ref = ''
    res = re.findall(r'(?:Ref No\.?|Txn ID|ref no|Ref\:|transaction number)\s*(\d{11,12})', text)
    if len(res) > 0:
        txn_ref += res[0]
    else :
        txn_ref = 'N/A'

    #---- Source // this part will fetch data from the database about the source.

    txn_source = ''

    if 'SBI'.lower() in text.lower():
        txn_source += 'SBI'
    elif 'Union Bank'.lower() in text.lower():
        txn_source += 'Union Bank'
    elif ('Food Wallet'.lower() in text.lower()) or ('Paytm'.lower() in text.lower()):
        txn_source += 'Paytm Wallet'


    #---- Mode
    txn_mode = 'Cashless'

    report = '''Datetime : {}
Amount : {}
Transaction ID : {}
Type : {}
Source : {}
Mode : {}'''.format(dt_string, txn_amt, txn_ref, txn_type, txn_source, txn_mode)

    print(report)
    return (report)


    # return "Processing report."

@bot.message_handler(content_types=['text'])
def expense_message(msg):
    txn_msg = msg.text
    detail_msg = expense_report(txn_msg)
    bot.reply_to(msg, detail_msg)


bot.infinity_polling()





