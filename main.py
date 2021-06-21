import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import config
from db_manager import DB_manager
from handlers import StartHandler, AddDeparture, MyDepartures, Other

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

db_manager = DB_manager()

def main():
    updater = Updater(config.TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', StartHandler))
    dispatcher.add_handler(MessageHandler(Filters.regex("Добавить отправление ➕"), AddDeparture))
    dispatcher.add_handler(MessageHandler(Filters.regex("Назад ◀️"), StartHandler))
    dispatcher.add_handler(MessageHandler(Filters.regex("Мои отправления ✉"), MyDepartures))
    dispatcher.add_handler(MessageHandler(Filters.text, Other))

    updater.start_polling()


if __name__ == '__main__':
    main()
