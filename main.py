from telegram.ext import Updater, CommandHandler, MessageHandler, filters
import pandas as pd

# Lug‘atni yuklash
try:
    data = pd.read_csv("lugat.csv", encoding="utf-8")
except FileNotFoundError:
    data = None
    print("Lug‘at fayli topilmadi. Iltimos, lugat.csv faylini loyihaga joylashtiring.")

# So‘z qidirish funksiyasi
def find_word(word):
    if data is not None and word in data["so'z"].values:
        return f"'{word}' lug‘atda mavjud."
    else:
        return f"'{word}' lug‘atda topilmadi."

# /start komandasi
def start(update, context):
    update.message.reply_text("Assalomu alaykum! So‘z kiriting va men uning to‘g‘ri variantini topaman.")

# Xabarlarni qayta ishlash
def handle_message(update, context):
    user_input = update.message.text.strip()
    response = find_word(user_input)
    update.message.reply_text(response)

# Asosiy funksiya
def main():
    # Telegram bot tokeningizni shu yerga kiriting
    updater = Updater("1916436179:AAGH0Jxf7E78D0N_bvmXBpUEghJeLvoI4h4")

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Botni ishga tushirish
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
