from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import pandas as pd
from difflib import get_close_matches

# Lug'atni yuklash
data = pd.read_csv("lugat.csv")  # Lug'at ma'lumotlari

# So'z qidirish funksiyasi
def find_word(word):
    if word in data["so'z"].values:
        return f"'{word}' lug‘atda mavjud."
    else:
        # O'xshash so'zlarni taklif qilish
        suggestions = get_close_matches(word, data["so'z"].values, n=3, cutoff=0.6)
        if suggestions:
            return f"'{word}' topilmadi. Sizning so'zingizga yaqin variantlar: {', '.join(suggestions)}"
        else:
            return f"'{word}' lug‘atda topilmadi."

# Bot funksiyalari
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Assalomu alaykum! So'z kiriting va men uning to'g'ri variantini topaman.")

def handle_message(update: Update, context: CallbackContext):
    user_input = update.message.text.strip()
    response = find_word(user_input)
    update.message.reply_text(response)

# Botni ishga tushirish
def main():
    updater = Updater("1916436179:AAGH0Jxf7E78D0N_bvmXBpUEghJeLvoI4h4", use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
