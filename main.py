from PIL import Image
import config
import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as BS
import random
import ipaddress
#import logging
#logging.info('This is an info message')
#logging.warning('This is a warning message')
#logging.error('This is an error message')
#logging.critical('This is a critical message')


r = requests.get('https://sinoptik.ua/погода-москва')
html = BS(r.content, 'html.parser')
bot = telebot.TeleBot(config.token)


for el in html.select('#content'):
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text
    text = el.select('.wDescription .description')[0].text
    den = el.select('.infoTimes .clock .descr')[0].text
    prazdnik = el.select('.oDescription .rSide')[0].text


@bot.callback_query_handler(func=lambda call: True)

def callbac_worker(call):
    
    # Если нажали на одну из 12 кнопок — выводим гороскоп

    if call.data == "zodiac": 

        # Формируем гороскоп

        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)

        # Отправляем текст в Телеграм

        bot.send_message(call.message.chat.id, msg)

    
@bot.message_handler(commands=['goroscop', 'help'])
def main(message):
	bot.send_message(message.chat.id, "Привет, погода на сегодня:\n" +
        t_min + ', ' + t_max + '\n' + text + '\n' +
        den + ', ' '\n' + prazdnik)
    


# Импортируем типы из модуля, чтобы создавать кнопки

#from telebot import types

# Заготовки для трёх предложений

first = ["Сегодня — идеальный день для новых начинаний."]


second = ["Но помните, что даже в этом случае нужно не забывать про","Если поедете за город, заранее подумайте про","Те, кто сегодня нацелен выполнить множество дел, должны помнить про","Если у вас упадок сил, обратите внимание на","Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]


second_add = ["отношения с друзьями и близкими.","работу и деловые вопросы, которые могут так некстати помешать планам.","себя и своё здоровье, иначе к вечеру возможен полный раздрай.","бытовые вопросы — особенно те, которые вы не доделали вчера.","отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]


third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.","Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.","Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.","Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.","Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]


# Метод, который получает сообщения и обрабатывает их

@bot.message_handler(content_types=['text'])

def get_text_messages(message):

    # Если написали «Привет»

    if message.text == "Хочу знать":

        # Пишем приветствие

        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")
        # вызов картинки средствами API TELEBOT
        bot.send_photo(message.from_user.id, open('cat.jpg', 'rb'))

        # Готовим кнопки

        keyboard = types.InlineKeyboardMarkup()

        # По очереди готовим текст и обработчик для каждого знака зодиака

        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')

        # И добавляем кнопку на экран

        keyboard.add(key_oven)

        key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')
        

        keyboard.add(key_telec)

        key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')

        keyboard.add(key_bliznecy)

        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')

        keyboard.add(key_rak)

        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')

        keyboard.add(key_lev)

        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')

        keyboard.add(key_deva)

        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')

        keyboard.add(key_vesy)

        key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')

        keyboard.add(key_scorpion)

        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')

        keyboard.add(key_strelec)

        key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')

        keyboard.add(key_kozerog)

        key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')

        keyboard.add(key_vodoley)

        key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')

        keyboard.add(key_ryby)

     

        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
        #bot.send_photo(message.from_user.id, open('cat.jpg', 'rb'))

    elif message.text == "панда":

        
        bot.send_photo(message.from_user.id, open('panda.jpg', 'rb'))
    else:

        bot.send_message(message.from_user.id, "Напиши  'Хочу знать' и будет счастье : )")
        bot.send_photo(message.from_user.id, open('panda.jpg', 'rb'))
        






@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп

    if call.data == "zodiac": 
        # Формируем гороскоп
        _msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
        #bot.send_message(call.message.chat.id, msg)
        





# Запускаем постоянный опрос бота в Телеграме


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
    
