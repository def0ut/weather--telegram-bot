import telebot
import datetime
import requests
from bs4 import BeautifulSoup

from aiogram import types

TOKEN = '5755775226:AAF0TWoZgN5PrkxSUcgX3AUOu2z-0737ZRA'
bot = telebot.TeleBot(TOKEN)


PC = '💾'

CITIES = ['1. Москва', '2. Санкт-Петербург', '3. Новосибирск', '4. Екатеринбург', '5. Казань',
                    '6. Нижний Новгород', '7. Челябинск', '8. Красноярск', '9. Cамара', '10. Уфа']

FORMAT_CITIES = f'.\n'.join(CITIES)


@bot.message_handler(commands=['start'])

def GET_START_INFORMATION(message):

    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}. 🙋🏻‍♂\n\n'
                                      f'Я мини-функциональный БОТ, который показывает ПОГОДУ.\n'
                                      f'На данный момент доступны города:\n\n{FORMAT_CITIES + "."}'
                                      f'\n\n'
                                      f'Чтобы продолжить напиши любой город из этого списка.')


@bot.message_handler(content_types=['text'])

def GET_WEATHER_IN__CITIES(message):

    # ПОГОДА В ГОРОДЕ - МОСКВА.

    if message.text.lower() == 'москва':

        URL_MOSCOW = 'https://sinoptik.ua/погода-москва'
        MOSCOW = requests.get(URL_MOSCOW)
        html = BeautifulSoup(MOSCOW.content, 'html.parser')

        for ELEMENTS in html.select('#content'):
            MINIMUM_TEMPERATURE_IN_MOSCOW = ELEMENTS.select('.min')[0].text
            MAXIMUM_TEMPERATURE_IN_MOSCOW = ELEMENTS.select('.max')[0].text
            CURRENT_TEMPERATURE_IN_MOSCOW = ELEMENTS.find('p', class_='today-temp').string.strip()
        bot.send_message(
            message.chat.id, f'☁️️️ Погода в городе Москва на сегодня:\n\n'
                             f'• Минимальная температура: {str(MINIMUM_TEMPERATURE_IN_MOSCOW)[4:]}\n'
                             f'• Максимальная температура: {str(MAXIMUM_TEMPERATURE_IN_MOSCOW)[5:]}\n'
                             f'• Текущая температура: {str(CURRENT_TEMPERATURE_IN_MOSCOW)[:-1]}'
    )

    # ПОГОДА В ГОРОДЕ - САНКТ ПЕТЕРБУРГ.

    elif message.text.lower() == 'санкт-петербург':

        URL_SPB = 'https://sinoptik.ua/погода-санкт-петербург'
        SPB = requests.get(URL_SPB)
        html = BeautifulSoup(SPB.content, 'html.parser')

        for ELEMENTS in html.select('#content'):
            MINIMUM_TEMPERATURE_IN_SPB = ELEMENTS.select('.min')[0].text
            MAXIMUM_TEMPERATURE_IN_SPB = ELEMENTS.select('.max')[0].text
            CURRENT_TEMPERATURE_IN_SPB= ELEMENTS.find('p', class_='today-temp').string.strip()
        bot.send_message(
            message.chat.id, f'☁️ Погода в городе Санкт-Петербург на сегодня:\n\n'
                             f'• Минимальная температура: {str(MINIMUM_TEMPERATURE_IN_SPB)[4:]}\n'
                             f'• Максимальная температура: {str(MAXIMUM_TEMPERATURE_IN_SPB)[5:]}\n'
                             f'• Текущая температура: {str(CURRENT_TEMPERATURE_IN_SPB)[:-1]}'
    )

    # ПОГОДА В ГОРОДЕ - НОВОСИБИРСК.

    elif message.text.lower() == 'новосибирск':

        URL_NOVOSIBIRSK = 'https://sinoptik.ua/погода-новосибирск'
        NOVOSIBIRSK = requests.get(URL_NOVOSIBIRSK)
        html = BeautifulSoup(NOVOSIBIRSK.content, 'html.parser')

        for ELEMENTS in html.select('#content'):
            MINIMUM_TEMPERATURE_IN_NOVOSIBIRSK = ELEMENTS.select('.min')[0].text
            MAXIMUM_TEMPERATURE_IN_NOVOSIBIRSK = ELEMENTS.select('.max')[0].text
            CURRENT_TEMPERATURE_IN_NOVOSIBIRSK = ELEMENTS.find('p', class_='today-temp').string.strip()
        bot.send_message(
            message.chat.id, f'☁️ Погода в городе Новосибирск на сегодня:\n\n'
                             f'• Минимальная температура: {str(MINIMUM_TEMPERATURE_IN_NOVOSIBIRSK)[4:]}\n'
                             f'• Максимальная температура: {str(MAXIMUM_TEMPERATURE_IN_NOVOSIBIRSK)[5:]}\n'
                             f'• Текущая температура: {str(CURRENT_TEMPERATURE_IN_NOVOSIBIRSK)[:-1]}'
    )

    # ПОГОДА В ГОРОДЕ - ЕКАТЕРИНБУРГ.

    elif message.text.lower() == 'екатеринбург':

        URL_EKB = 'https://sinoptik.ua/погода-екатеринбург'
        EKB = requests.get(URL_EKB)
        html = BeautifulSoup(EKB.content, 'html.parser')

        for ELEMENTS in html.select('#content'):
            MINIMUM_TEMPERATURE_IN_EKB = ELEMENTS.select('.min')[0].text
            MAXIMUM_TEMPERATURE_IN_EKB = ELEMENTS.select('.max')[0].text
            CURRENT_TEMPERATURE_IN_EKB = ELEMENTS.find('p', class_='today-temp').string.strip()
        bot.send_message(
            message.chat.id, f'☁️ Погода в городе Екатеринбург на сегодня:\n\n'
                             f'• Минимальная температура: {str(MINIMUM_TEMPERATURE_IN_EKB)[4:]}\n'
                             f'• Максимальная температура: {str(MAXIMUM_TEMPERATURE_IN_EKB)[5:]}\n'
                             f'• Текущая температура: {str(CURRENT_TEMPERATURE_IN_EKB)[:-1]}'
    )

    # ПОГОДА В ГОРОДЕ - КАЗАНЬ.

    elif message.text.lower() == 'казань':

        URL_KZN = 'https://sinoptik.ua/погода-казань'
        KZN = requests.get(URL_KZN)
        html = BeautifulSoup(KZN.content, 'html.parser')

        for ELEMENTS in html.select('#content'):
            MINIMUM_TEMPERATURE_IN_KZN = ELEMENTS.select('.min')[0].text
            MAXIMUM_TEMPERATURE_IN_KZN = ELEMENTS.select('.max')[0].text
            CURRENT_TEMPERATURE_IN_KZN = ELEMENTS.find('p', class_='today-temp').string.strip()
        bot.send_message(
            message.chat.id, f'☁️ Погода в городе Казань на сегодня:\n\n'
                             f'• Минимальная температура: {str(MINIMUM_TEMPERATURE_IN_KZN)[4:]}\n'
                             f'• Максимальная температура: {str(MAXIMUM_TEMPERATURE_IN_KZN)[5:]}\n'
                             f'• Текущая температура: {str(CURRENT_TEMPERATURE_IN_KZN)[:-1]}'
    )

    # ПОГОДА В ГОРОДЕ - НИЖНИЙ НОВГОРОД.

    elif message.text.lower() == 'нижний новгород':

        URL_NN = 'https://sinoptik.ua/погода-нижний-новгород'
        NN = requests.get(URL_NN)
        html = BeautifulSoup(NN.content, 'html.parser')

        for ELEMENTS in html.select('#content'):
            MINIMUM_TEMPERATURE_IN_NN = ELEMENTS.select('.min')[0].text
            MAXIMUM_TEMPERATURE_IN_NN = ELEMENTS.select('.max')[0].text
            CURRENT_TEMPERATURE_NN = ELEMENTS.find('p', class_='today-temp').string.strip()
        bot.send_message(
            message.chat.id, f'☁️ Погода в городе Нижний Новогород на сегодня:\n\n'
                             f'• Минимальная температура: {str(MINIMUM_TEMPERATURE_IN_NN)[4:]}\n'
                             f'• Максимальная температура: {str(MAXIMUM_TEMPERATURE_IN_NN)[5:]}\n'
                             f'• Текущая температура: {str(CURRENT_TEMPERATURE_NN)[:-1]}'
    )

    # ПОГОДА В ГОРОДЕ - ЧЕЛЯБИНСК.

    elif message.text.lower() == 'челябинск':

        URL_CB = 'https://sinoptik.ua/погода-челябинск'
        CB = requests.get(URL_CB)
        html = BeautifulSoup(CB.content, 'html.parser')

        for ELEMENTS in html.select('#content'):
            MINIMUM_TEMPERATURE_IN_CB = ELEMENTS.select('.min')[0].text
            MAXIMUM_TEMPERATURE_IN_CB = ELEMENTS.select('.max')[0].text
            CURRENT_TEMPERATURE_IN_CB = ELEMENTS.find('p', class_='today-temp').string.strip()
        bot.send_message(
            message.chat.id, f'☁️ Погода в городе Челябинск на сегодня:\n\n'
                             f'• Минимальная температура: {str(MINIMUM_TEMPERATURE_IN_CB)[4:]}\n'
                             f'• Максимальная температура: {str(MAXIMUM_TEMPERATURE_IN_CB)[5:]}\n'
                             f'• Текущая температура: {str(CURRENT_TEMPERATURE_IN_CB)[:-1]}'
    )

    # ПОГОДА В ГОРОДЕ - КРАСНОЯРСК.

    elif message.text.lower() == 'красноярск':

        URL_KRN = 'https://sinoptik.ua/погода-красноярск'
        KRN = requests.get(URL_KRN)
        html = BeautifulSoup(KRN.content, 'html.parser')

        for ELEMENTS in html.select('#content'):
            MINIMUM_TEMPERATURE_IN_KRN = ELEMENTS.select('.min')[0].text
            MAXIMUM_TEMPERATURE_IN_KRN = ELEMENTS.select('.max')[0].text
            CURRENT_TEMPERATURE_IN_KRN = ELEMENTS.find('p', class_='today-temp').string.strip()
        bot.send_message(
            message.chat.id, f'☁️ Погода в городе Красноярск на сегодня:\n\n'
                             f'• Минимальная температура: {str(MINIMUM_TEMPERATURE_IN_KRN)[4:]}\n'
                             f'• Максимальная температура: {str(MAXIMUM_TEMPERATURE_IN_KRN)[5:]}\n'
                             f'• Текущая температура: {str(CURRENT_TEMPERATURE_IN_KRN)[:-1]}'
    )

    # ПОГОДА В ГОРОДЕ - САМАРА.

    elif message.text.lower() == 'самара':

        URL_SM = 'https://sinoptik.ua/погода-самара'
        SM = requests.get(URL_SM)
        html = BeautifulSoup(SM.content, 'html.parser')

        for ELEMENTS in html.select('#content'):
            MINIMUM_TEMPERATURE_IN_SM = ELEMENTS.select('.min')[0].text
            MAXIMUM_TEMPERATURE_IN_SM = ELEMENTS.select('.max')[0].text
            CURRENT_TEMPERATURE_IN_SM = ELEMENTS.find('p', class_='today-temp').string.strip()
        bot.send_message(
            message.chat.id, f'☁️ Погода в городе Самара на сегодня:\n\n'
                             f'• Минимальная температура: {str(MINIMUM_TEMPERATURE_IN_SM)[4:]}\n'
                             f'• Максимальная температура: {str(MAXIMUM_TEMPERATURE_IN_SM)[5:]}\n'
                             f'• Текущая температура: {str(CURRENT_TEMPERATURE_IN_SM)[:-1]}'
    )

    # ПОГОДА В ГОРОДЕ - УФА.

    elif message.text.lower() == 'уфа':

        URL_UFA = 'https://sinoptik.ua/погода-уфа'
        UFA = requests.get(URL_UFA)
        html = BeautifulSoup(UFA.content, 'html.parser')

        for ELEMENTS in html.select('#content'):
            MINIMUM_TEMPERATURE_IN_UFA = ELEMENTS.select('.min')[0].text
            MAXIMUM_TEMPERATURE_IN_UFA = ELEMENTS.select('.max')[0].text
            CURRENT_TEMPERATURE_IN_UFA = ELEMENTS.find('p', class_='today-temp').string.strip()
        bot.send_message(
            message.chat.id, f'☁️ Погода в городе Уфа на сегодня:\n\n'
                             f'• Минимальная температура: {str(MINIMUM_TEMPERATURE_IN_UFA)[4:]}\n'
                             f'• Максимальная температура: {str(MAXIMUM_TEMPERATURE_IN_UFA)[5:]}\n'
                             f'• Текущая температура: {str(CURRENT_TEMPERATURE_IN_UFA)[:-1]}'
    )

if __name__ == '__main__':
    bot.polling(none_stop=True)