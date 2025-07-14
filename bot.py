import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from terabox import extract_direct_link
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a Terabox video URL and I'll try to fetch the download link!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()
    if "terabox" not in url:
        await update.message.reply_text("Please send a valid Terabox link.")
        return

    await update.message.reply_text("Processing your link...")

    direct_link = extract_direct_link(url)
    if direct_link:
        await update.message.reply_text(f"✅ Download link:\n{direct_link}")
    else:
        await update.message.reply_text("❌ Failed to extract download link. Try a different URL or check the format.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
