import telegram
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext


def StartHandler(update: Update, context: CallbackContext):
    # b.write_user_position(update.message.chat_id, "main")
    print(f"New message from {update.message.chat_id} , text : {update.message.text}")

    keyboard = [
        [telegram.KeyboardButton("Добавить отправление ➕")],
        [telegram.KeyboardButton("Мои отправления ✉")]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard)
    update.message.reply_text('Пожалуйста выберете!', reply_markup=reply_markup)



def AddDeparture(update: Update, context: CallbackContext):
    # b.write_user_position(update.message.chat_id, "main")
    print(f"New message from {update.message.chat_id} , text : {update.message.text}")

    """keyboard = [
        [telegram.KeyboardButton("Добавить отправление ➕")],
        [telegram.KeyboardButton("Мои отправления ✉")]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard)"""

    update.message.reply_text("Трек номер:")



