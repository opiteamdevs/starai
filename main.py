import telebot

TOKEN = '9195985551:AAEturVMDDVOL7hSpHdxW3XDT2pgnE6AAMM'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def processar_mensagem(message):
    texto_usuario = message.text
    
    if "olá" in texto_usuario.lower() or "salve" in texto_usuario.lower():
       bot.reply_to(message, "Opa!!")
    elif "Qual teu nome?" in texto_usuario.lower():
        bot.reply_to(message, "Eu me chamo OpenSumo!")
    else:
        bot.reply_to(message, "Eu não entendi, repita dnv?")
print("Bot aguardando a tua lógica...")
bot.infinity_polling()
