import telebot
from datetime import datetime
import requests
import PIL.Image as Image
import io
import numpy as np
import cv2
import re


# If the script generates connection timed out error then uncomment the
# below line and execute the whole program
# requests.get('https://google.com', verify=False)

token = ''
with open('token.txt', 'r') as f:
    token = f.read()
    # print(token)

# tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

bot = telebot.TeleBot(token)

def expense_report(text):
    txn_keyword = ['SBI', 'Transaction', 'from', 'to', 'Paid', 'Paytm', 'Food Wallet', 'Rs', 'A/c',
                   'debited', 'credited', 'Ref', 'Ref No', 'transfer to', 'UPI', 'Txn ID', 'payment',
                   'successfully', 'succeeded', 'Union Bank of India', 'Union Bank', 'SBI Debit Card',
                   'NEFT', 'UTR', 'PhonePe', 'Google Pay', 'Gpay', 'debit', 'credit', 'cash', 'IFSC',
                   'IMPS', 'Payment Gateway', 'failed']

    if not (any(x.lower() in text.lower() for x in txn_keyword)):
        return "This is not a transaction message."

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
To : N/A
From : Wallet
Mode : Cash'''.format(dt_string, amount[0], type)


        return report

    return "Processing report."

@bot.message_handler(content_types=['text'])
def expense_message(msg):
    txn_msg = msg.text
    detail_msg = expense_report(txn_msg)
    bot.reply_to(msg, detail_msg)


# @bot.message_handler(content_types=['photo'])
# def expense_receipt(message):
#     # bot.reply_to(message, "This is a picture.")
#     print('message.photo =', message.photo)
#     fileID = message.photo[-1].file_id
#     print('fileID =', fileID)
#     file_info = bot.get_file(fileID)
#     print('file.file_path =', file_info.file_path)
#     receipt = bot.download_file(file_info.file_path)
#     img = Image.open(io.BytesIO(receipt))
#     img.save(r'C:\Users\amiab\Projects\Expense Manager\media\img.jpg')
#     img = cv2.imread(r'C:\Users\amiab\Projects\Expense Manager\media\img.jpg')
#     text = increase_accuracy(img)
#     # print(text)
#     bot.reply_to(message, text)


    # img.save(r'C:\Users\amiab\Projects\Expense Manager\media\img3.jpg')
    #To download the receipt
    # with open("C:\\Users\\amiab\\Projects\Expense Manager\\media\\image.jpg", 'wb') as new_file:
    #     new_file.write(receipt)


bot.infinity_polling()





