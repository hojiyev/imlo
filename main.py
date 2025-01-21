from telegram.ext import Application, CommandHandler, MessageHandler, filters
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
async def start(update, context):
    await update.message.reply_text("Assalomu alaykum! So‘z kiriting va men uning to‘g‘ri variantini topaman.")

# Xabarlarni qayta ishlash
async def handle_message(update, context):
    user_input = update.message.text.strip()
    response = find_word(user_input)
    await update.message.reply_text(response)

# Asosiy funksiya
def main():
    # Telegram bot tokeningizni shu yerga kiriting
    application = Application.builder().token("1916436179:AAGH0Jxf7E78D0N_bvmXBpUEghJeLvoI4h4").build()

    # Komandalar va xabarlarni qo‘shish
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Botni ishga tushirish
    application.run_polling()

if __name__ == "__main__":
    main()