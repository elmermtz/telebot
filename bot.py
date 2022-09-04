import time
from config import *
import telebot

# Se instancia el bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# responde a comando citando
@bot.message_handler(commands=["start", "ayuda", "help"])
def cmd_start(message):
    bot.reply_to(message, "Hola!. Como andamios?")

# responde a texto
@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    if message.text.startswith("/"):
        # envia al chat.id de donde vien el request el siguiente texto
        bot.send_message(message.chat.id, "comando no disponible")
        
    else:
        x = bot.send_message(message.chat.id, "<b>HOLA</b>", parse_mode="html", disable_web_page_preview=True)
        time.sleep(3)
        bot.edit_message_text("<u>ADIOS</u>", message.chat.id, x.message_id, parse_mode="html")


# MAIN#####################################

if __name__ == '__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('Fin')
