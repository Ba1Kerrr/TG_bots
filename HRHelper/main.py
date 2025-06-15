import telebot
from telebot import types
bot = telebot.TeleBot('YOUR_BOT_TOKEN')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я HRHelper. Я помогу вам с кадровыми задачами.')
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Опубликовать вакансию':
        bot.send_message(message.chat.id, 'Пожалуйста, введите информацию о вакансии.')
        bot.register_next_step_handler(message, publish_vacancy)
def publish_vacancy(message):
    vacancy_info = message.text
    # Обработка публикации вакансии
    bot.send_message(message.chat.id, 'Вакансия опубликована!')
bot.polling()