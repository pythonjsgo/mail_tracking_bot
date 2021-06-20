import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import config
from handlers import StartHandler, AddDeparture


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def main():
    updater = Updater(config.TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', StartHandler))
    dispatcher.add_handler(MessageHandler(Filters.regex("Добавить отправление ➕"), AddDeparture))

    updater.start_polling()


if __name__ == '__main__':
    main()
