import telebot

bot = telebot.TeleBot('1104778803:AAHv9g6lHKJ6-T7UJL54KHEcYcm5AXSFASQ')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()