import telebot
bot = telebot.TeleBot('my token')
# Start "Welcome" message
#@bot.message_handler(commands=['start'])
#def start_message(message):
#    bot.send_message(message.chat.id, "О, {0.first_name}! \n Приветики-пистолетики, поговорим? ".format(message.from_user))

# Talks
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, "О, {0.first_name}! \nПриветики-пистолетики, поговорим? ".format(message.from_user))
    elif message.text.lower() == 'что ты умеешь?' or message.text.lower() =='уу':
        bot.send_message(message.chat.id, 'нн')
    elif message.text.lower() == 'мне скучно':
        bot.send_message(message.chat.id, 'У меня есть шутка')
    elif message.text.lower() == 'какая':
        bot.send_message(message.chat.id, 'Говорят, после курсов по раскрытию паранормальных способностей, лучшие выпускники уходят в ясновидящие, а худшие в гидрометцентр')
    elif message.text.lower() == 'не смешно':
        bot.send_message(message.chat.id, 'ой, всё!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    elif message.text.lower() == 'что ты умеешь?':
        bot.send_sticker(message.chat.id, 'Шутить')
    else:
        bot.send_message(message.chat.id, 'эм, не понял')

#def joke (message:)
#def worldwide_search (message):
bot.polling()