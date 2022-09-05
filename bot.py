import time
from config import *
import telebot

# Se instancia el bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# responde a comando citando
@bot.message_handler(commands=["start", "ayuda", "help"])
def cmd_start(message):
    bot.reply_to(message, "Hola!. Como andamios?")

# ENVIAR DOCUMENTO
@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    # si el mensaje de texto empieza con /
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "comando no disponible")
    

    # de lo contrario
    else:
        
        archivo = open("./docs/lukas.odt", "rb")
        #  envia al chat.id de donde vien el request el siguiente archivo
        bot.send_document(message.chat.id, archivo, caption="DOCUMENTO")


# MAIN#####################################

if __name__ == '__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('Fin')
