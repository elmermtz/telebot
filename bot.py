from config import *
import telebot

# Se instancia el bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# responde a comando citando
@bot.message_handler(commands=["start", "ayuda", "help"])
def cmd_start(message):
    bot.reply_to(message, "Hola!. Como andamios?")

@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "comando no disponible")
    else:
        bot.send_message(message.chat.id, "sucribete a mi canal")


# MAIN#####################################

if __name__ == '__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('Fin')
