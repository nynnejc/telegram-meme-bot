from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import random
import config

def start(update, context):
    update.message.reply_text("🖤🖤🖤🖤🖤🖤🖤")

def help(update, context):
    update.message.reply_text("it is help")

def echo(update, context):
    img = ["img/happyduck.jpg", "img/pspsps.jpg", "img/trashcan.jpg", "img/8hours.jpg", "img/aaaa.jpg", "img/bday.jpg" ]
    random.shuffle(img)
    
    context.bot.send_photo(chat_id=update.message.chat.id, photo=open(img[0], 'rb'))

updater = Updater(token=config.BOT_TOKEN, use_context=True)

dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()