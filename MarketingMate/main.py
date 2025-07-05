import telebot
from telebot import types
import os
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv('TG_API_key'))
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('Рассылка подписчикам')
    button2 = types.KeyboardButton('Управление подписчиками')
    button3 = types.KeyboardButton('Рассылка контента')
    button4 = types.KeyboardButton('Управление кампаниями')
    button5 = types.KeyboardButton('Назад')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5)
    bot.send_message(message.chat.id, 'Привет! Я MarketingMate. Я помогу вам автоматизировать маркетинг.', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def answer_message(message):
    if message.text == 'Рассылка подписчикам':
        # Обработка нажатия кнопки "Рассылка подписчикам"
        newsletter_special_offer(message)
    elif message.text == 'Управление подписчиками':
        # Обработка нажатия кнопки "Управление подписчиками"
        subs_management(message)
    elif message.text == 'Рассылка контента':
        # Обработка нажатия кнопки "Рассылка контента"
        newsletter_offer(message)
    elif message.text == 'Управление кампаниями':
        # Обработка нажатия кнопки "Управление кампаниями"
        compaign_management(message)
    elif message.text == 'Назад':
        # Обработка нажатия кнопки "Назад"
        back(message)

def subs_management(message):
    markup = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('Добавить подписчика')
    button2 = types.KeyboardButton('Удалить подписчика')
    button3 = types.KeyboardButton('Вывести всех подписчиков')
    button4 = types.KeyboardButton('Назад')
    markup.row(button1, button2, button3)
    markup.row(button4)
    bot.send_message(message.chat.id, 'Вы выбрали управление подписчиками.', reply_markup=markup)
    if message.text == 'Добавить подписчика':
            bot.send_message(message.chat.id, 'Вы выбрали добавить подписчика.')
            bot.send_message(message.chat.id, 'Пожалуйста, введите ID пользователя и id чата.')
            msg = bot.wait_for_message(chat_id=message.chat.id)
            add_subscriber(msg)
            button1 = types.KeyboardButton('Добавить подписчика')
            button2 = types.KeyboardButton('Удалить подписчика')
            button3 = types.KeyboardButton('Вывести всех подписчиков')
            button4 = types.KeyboardButton('Назад')
            markup.row(button1, button2, button3)
            markup.row(button4)

    if message.text == 'Удалить подписчика':
            bot.remove_chat_member('chat_id', 'user_id')
            bot.send_message(message.chat.id, 'Подписчик удален!')
    if message.text == 'get subscribers':
            bot.get_chat_members('chat_id')
    # Обработка нажатия кнопок
    def add_subscriber(msg):
            bot.add_chat_member('chat_id', 'user_id')
            bot.send_message(message.chat.id, 'Подписчик добавлен!')
    
def newsletter_special_offer(message):
    bot.send_message(message.chat.id, 'Вы выбрали рассылку подписчикам специального предложения.')
    bot.send_message(message.chat.id, 'Пожалуйста, введите сообщение которое надо отправить.')

def automate_marketing(message):
    marketing_info = message.text
    # Обработка автоматизации маркетинга
    bot.send_message(message.chat.id, 'Маркетинг автоматизирован!')

def newsletter_offer(message):
    bot.send_message(message.chat.id, 'Вы выбрали рассылку подписчикам.')
    bot.send_message(message.chat.id, 'Пожалуйста, введите сообщение которое надо отправить.')

def analitics(message):
    bot.send_message(message.chat.id, 'Вы выбрали анализ.')
    bot.send_message(message.chat.id, 'Пожалуйста, введите сообщение которое надо отправить.')

def compaign_management(message):
    bot.send_message(message.chat.id, 'Вы выбрали управление кампанией.')
    bot.send_message(message.chat.id, 'Пожалуйста, введите сообщение которое надо отправить.')

def back(message):
    bot.send_message(message.chat.id, 'Вы вернулись на главную страницу.')
    bot.edit_message_reply_markup(message.chat.id, message.message_id, reply_markup=None)

bot.polling(none_stop=True)
