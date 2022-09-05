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
# aqui el type puede recibir textos y fotos
@bot.message_handler(content_types=["text", "photo"])
def bot_mensajes_texto(message):
    # si el mensaje cumple CON LAS DOS REQUERIMIENTOS entonces es TRUE, sino pasara a else
    if message.text and message.text.startswith("/"):
        bot.send_message(message.chat.id, "comando no disponible")
    

    # de lo contrario
    else:
        # muestra la accion que esta llevando a cabo el bot
        bot.send_chat_action(message.chat.id, "upload_document")
        archivo = open("./docs/lukas.odt", "rb")
        #  envia al chat.id de donde vien el request el siguiente archivo
        bot.send_document(message.chat.id, archivo, caption="DOCUMENTO")

    # if message.photo:
    #     bot.send_message(message.chat.id, "que linda photo")

    # else:
    #     pass


# MAIN#####################################

if __name__ == '__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('Fin')
