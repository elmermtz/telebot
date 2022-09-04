import time
from config import *
import telebot

# Se instancia el bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# responde a comando citando
@bot.message_handler(commands=["start", "ayuda", "help"])
def cmd_start(message):
    bot.reply_to(message, "Hola!. Como andamios?")

# borra mensaje de texto en 3 segundos
@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    # si el mensaje de texto empieza con /
    if message.text.startswith("/"):
        # envia al chat.id de donde vien el request el siguiente texto
        bot.send_message(message.chat.id, "comando no disponible")

    # de lo contrario
    else:
        # envia mensaje al chatid del message recibido en formato html
        # x = bot.send_message(message.chat.id, "<b>HOLA</b>", parse_mode="html", disable_web_page_preview=True)
        # espere 3 segundos
        time.sleep(3)
        # Borra mensaje x enviado por CLIENTE, necesita chat_id y message_id para borrarlo
        # el message_id lo toma del objeto message
        bot.delete_message(message.chat.id, message.message_id)


# MAIN#####################################

if __name__ == '__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('Fin')
