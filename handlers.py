import telegram
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackContext

import config
from db_manager import DB_manager

db_manager = DB_manager()
bot = telegram.Bot(token=config.TOKEN)


def StartHandler(update: Update, context: CallbackContext):
    # b.write_user_position(update.message.chat_id, "main")

    print(f"New message from {update.message.chat_id} , text : {update.message.text}")


    user_id = update.message.from_user.id
    if not db_manager.user_exist(user_id): db_manager.add_user(user_id)
    db_manager.update_user_position(user_id, "StartHandler")
    db_manager.debug_info()

    keyboard = [
        [telegram.KeyboardButton("Добавить отправление ➕")],
        [telegram.KeyboardButton("Мои отправления ✉")]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard)
    update.message.reply_text('Пожалуйста выберете!', reply_markup=reply_markup)


def AddDeparture(update: Update, context: CallbackContext):
    # b.write_user_position(update.message.chat_id, "main")
    print(f"New message from {update.message.chat_id} , text : {update.message.text}")


    user_id = update.message.from_user.id
    db_manager.update_user_position(user_id, "AddDeparture")
    db_manager.debug_info()

    keyboard = [
        [telegram.KeyboardButton("Назад ◀️")],
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard)
    update.message.reply_text("Трек номер:", reply_markup=reply_markup)


def MyDepartures(update: Update, context: CallbackContext):
    print(f"New message from {update.message.chat_id} , text : {update.message.text}")


    user_id = update.message.from_user.id
    db_manager.update_user_position(user_id, "MyDepartures")
    db_manager.debug_info()

    keyboard = [
        [telegram.KeyboardButton("Назад ◀️")],
    ]

    if len(db_manager.get_user_departures(user_id)) == 0:
        departures = "Нет отправлений"
    else:
        departures = db_manager.get_user_departures(user_id)

    reply_markup = ReplyKeyboardMarkup(keyboard)
    update.message.reply_text(departures, reply_markup=reply_markup)


def Other(update: Update, context: CallbackContext):
    # b.write_user_position(update.message.chat_id, "main")

    user_id = update.message.from_user.id
    position = db_manager.get_user_position(user_id)[0]
    db_manager.debug_info()
    if position == "AddDeparture":
        db_manager.add_user_departures(user_id, update.message.text)
        bot.send_message(update.message.chat_id, )


    print(f"New message from {update.message.chat_id} , text : {update.message.text}")


"""
def Back(update: Update, context: CallbackContext):
    # b.write_user_position(update.message.chat_id, "main")
    db_manager = DB_manager()
    user_id = update.message.from_user.id
    position = db_manager.get_user_position(user_id)
    db_manager.debug_info()
    StartHandler(update, context)

    print(f"New message from {update.message.chat_id} , text : {update.message.text}")
"""
