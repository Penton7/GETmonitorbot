import requests
import telebot
import time

token = '' #Токен телеграмма
url = ''   #Сайт который нужно монторить
id =  ' '     #айди чата. (узнаем через https://api.telegram.org/bot $token$ /getUpdates)

bot = telebot.TeleBot(token)

bot.send_message(id, 'Bot started')
def status_check():
    try:
        response = requests.get(url, timeout=(100))
        print(response)

    #except requests.exceptions.ReadTimeout as e:
        #print('Oops. Read timeout occured')
        #bot.send_message(id, e)

    except requests.exceptions.ConnectTimeout as x:
        print('Oops. Connection timeout occured!')
        bot.send_message(id, " Connection to " + url + " timed out ")


while True:
    status_check()
    time.sleep(300) #переодичность опроса
