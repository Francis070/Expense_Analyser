import telebot
import requests
import PIL.Image as Image
import io
import pytesseract as tess
import numpy as np
import cv2
import re


# If the script generates connection timed out error then uncomment the
# below line and execute the whole program
requests.get('https://google.com', verify=False)

token = ''
with open('token.txt', 'r') as f:
    token = f.read()
    # print(token)

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

bot = telebot.TeleBot(token)

def increase_accuracy(img):
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    img = cv2.GaussianBlur(img, (5, 5), 0)

    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    text = tess.image_to_string(img, lang="eng")
    return text

def extract_info(text):


@bot.message_handler(commands=['run'])
def send_welcome(message):
    bot.reply_to(message, "You can send Expense Receipts or forward Transaction messages.")

@bot.message_handler(content_types=['text'])
def expense_message(msg):
    bot.reply_to(msg, "This is a text.")


@bot.message_handler(content_types=['photo'])
def expense_receipt(message):
    # bot.reply_to(message, "This is a picture.")
    print('message.photo =', message.photo)
    fileID = message.photo[-1].file_id
    print('fileID =', fileID)
    file_info = bot.get_file(fileID)
    print('file.file_path =', file_info.file_path)
    receipt = bot.download_file(file_info.file_path)
    img = Image.open(io.BytesIO(receipt))
    img.save(r'C:\Users\amiab\Projects\Expense Manager\media\img.jpg')
    img = cv2.imread(r'C:\Users\amiab\Projects\Expense Manager\media\img.jpg')
    text = increase_accuracy(img)
    # print(text)
    bot.reply_to(message, text)


    # img.save(r'C:\Users\amiab\Projects\Expense Manager\media\img3.jpg')
    #To download the receipt
    # with open("C:\\Users\\amiab\\Projects\Expense Manager\\media\\image.jpg", 'wb') as new_file:
    #     new_file.write(receipt)


bot.infinity_polling()





