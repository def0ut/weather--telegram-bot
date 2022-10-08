
# ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И ПАКЕТОВ

import telebot
import datetime
import requests
from bs4 import BeautifulSoup

import config

from aiogram import types

# ПОДКЛЮЧЕНИЕ ТОКЕНА ДЛЯ ИСПОЛЬЗОВАНИЯ БОТА В ТЕЛЕГРАМ

bot = telebot.TeleBot(config.TOKEN)

# КОДИНГ БОТА

@bot.message_handler(commands=['start'])

def GET_START_INFORMATION(message):

    bot.send_message(message.chat.id,
                    f'Привет, {message.from_user.first_name}. 🙋🏻‍♂\n'
                    f'Я мини-функциональный БОТ, который показывает ПОГОДУ.\n\n'
                    
                    f'Чтобы продолжить введите любой город.'

    )

@bot.message_handler(content_types=['text'])

def GET_WEATHER_IN_CITIES(message):

    URL = f'https://sinoptik.ua/погода-{message.text.lower()}'
    r = requests.get(URL)
    HTML = BeautifulSoup(r.content, 'html.parser')
    for ELEMENTS in HTML.select('#content'):
        MINIMAL_TEMP = ELEMENTS.select('.min')[0].text
        MAXIMUM_TEMP = ELEMENTS.select('.max')[0].text
        CURRENT_TEMP = ELEMENTS.find('p', {'class':'today-temp'}).string.strip()

        bot.send_message(
            message.chat.id, f'☁️ Погода в городе {message.text.upper()[0] + message.text.lower()[1:]} на сегодня:\n\n'
                             f'• Минимальная температура: {str(MINIMAL_TEMP)[4:]}\n'
                             f'• Максимальная температура: {str(MAXIMUM_TEMP)[5:]}\n'
                             f'• Текущая температура: {str(CURRENT_TEMP)[:-1]}'
    )


if __name__ == '__main__':
    bot.polling(none_stop=True)