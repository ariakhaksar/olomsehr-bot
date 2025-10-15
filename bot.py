import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام ببعی 🌸 من ربات سید جعفر حسینی هستم و آماده‌ام!")

# پاسخ به پیام‌های عادی (اختیاری)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"شما گفتی: {text}")

# اجرای ربات
def main():
    token = os.getenv("BOT_TOKEN")  # توکن از GitHub Secrets گرفته می‌شود
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    app.run_polling()

if __name__ == "__main__":
    main()
  Update bot.py
