import telebot

API_TOKEN = '7899000276:AAFfOLD2LRPlelvobd-T6Ni0uZEMw-t_lwE'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Teacher Brian Bot!\nAapka message submit ho gaya hai.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Message Received: " + message.text)

bot.polling(non_stop=True)
