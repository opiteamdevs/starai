import os
import telebot

# O token sagrado que o BotFather te deu no print! 🤖
TOKEN = '9217841403:AAFZ83Lv5tJrozGzTFgBDXvaQjh401r3q1k'
bot = telebot.TeleBot(TOKEN)

# Resposta zoeira para quando o bot finalmente acordar
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Opa, salve mestre do 5° ano! 🍔🤖 A inteligência foi aplicada com sucesso. Ixe lá ele, tá apertano no buraco ixe 😳")

# Qualquer outra mensagem que mandarem para o bot
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Eu te escutei, mas eu ainda não tenho cérebro")

if __name__ == '__main__':
    print("O robô acordou da Matrix e está rodando na nuvem...")
    bot.infinity_polling()
  
