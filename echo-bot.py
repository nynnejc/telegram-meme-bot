#!/usr/bin/env python
# pylint: disable=C0116
# This program is dedicated to the public domain under the CC0 license.

import logging
import traceback

from telegram import Update, ParseMode
from telegram.ext import Updater, CallbackContext, CommandHandler, Filters

import config

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

BOT_TOKEN = config.BOT_TOKEN

def main() -> None:

    updater = Updater(BOT_TOKEN)


    dispatcher = updater.dispatcher

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()