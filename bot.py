from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Tokeningizni shu yerga yozing
TOKEN = "8234701116:AAHd9KqH2__HZltfht0RM-98-aF978YRHhI"

def start(update, context):
    update.message.reply_text("Salom! Men 54-maktam 11-sinf uchun yaratilgan botman 🤖\n\nMenyu uchun /menu yozing.")

def menu(update, context):
    keyboard = [
        ["1. O‘quvchilar soni"],
        ["2. O‘quvchilar F.I.Sh"],
        ["3. Ota-onalar telefon raqami"],
        ["4. Ota-ona F.I"],
        ["5. Uy manzillari"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("Kerakli bo‘limni tanlang:", reply_markup=reply_markup)

def handle_message(update, context):
    text = update.message.text

    if text == "1. O‘quvchilar soni":
        update.message.reply_text("Hozircha: 25 ta o‘quvchi bor 📊")
    elif text == "2. O‘quvchilar F.I.Sh":
        update.message.reply_text("O‘quvchilar ro‘yxati: \n1. Abdujamilov Yo'ldosh\n2. Absoatov Farux\n...")
    elif text == "3. Ota-onalar telefon raqami":
        update.message.reply_text("Tel raqamlar: \nAbdujamilov Yo'ldoshningning otasi: +998993792224\n...")
    elif text == "4. Ota-ona F.I":
        update.message.reply_text("Ota-onalar ro‘yxati: \n1. Abdujamilov Yo'ldosh\n2. Musirov Erkin\n...")
    elif text == "5. Uy manzillari":
        update.message.reply_text("Manzillar: \n1. Surxondaryo, Jarqurgon, Xalqobod mahallasi, olmos koʻchasi 91-uy...\n")
    else:
        update.message.reply_text("Iltimos, menyudan tanlang yoki /menu yozing.")

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("menu", menu))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

updater.start_polling()
updater.idle()