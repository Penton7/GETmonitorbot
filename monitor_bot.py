import urllib.request
import telebot
import time

token = '' #Токен телеграмма
url = ''   #Сайт который нужно монторить
id =       #айди чата. (узнаем через https://api.telegram.org/bot $token$ /getUpdates)

response = urllib.request.urlopen(url)

bot = telebot.TeleBot(token)

bot.send_message(id, 'Bot started')
def status_check():
    response.getcode()
    print(response.getcode())

    if response.getcode() == 200:
        print('norm')
    else:
        bot.send_message(id, 'Сервер упал.')


while True:
    status_check()
    time.sleep(300) #переодичность опроса
