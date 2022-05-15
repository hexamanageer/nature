import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['charizard'])
def charizard(message):
  bot.reply_to(message, "Best - Timid, modest")
  
bot.polling()
