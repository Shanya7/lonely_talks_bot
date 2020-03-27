import telebot

bot = telebot.TeleBot('my_token')
# Start "Welcome" message
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "О! {0.first_name}! \n сто лет не видились".format(message.from_user))

bot.polling()
