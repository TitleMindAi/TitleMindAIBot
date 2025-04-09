
import os
from flask import Flask, request
import telegram
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telegram.Bot(token=TELEGRAM_TOKEN)

app = Flask(__name__)

@app.route(f"/{TELEGRAM_TOKEN}", methods=["POST"])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    message_text = update.message.text if update.message else ""
    print(f"✅ Telegram webhook hit | Message from {chat_id}: {message_text}")

    if message_text == "/start":
        bot.send_message(chat_id=chat_id, text="👋 Welcome to TitleMind AI. Please upload your first document.")
    elif message_text == "/reset_headers":
        bot.send_message(chat_id=chat_id, text="✅ Your saved Excel column headers have been cleared.")
    elif message_text == "/help":
        bot.send_message(chat_id=chat_id, text="📎 Upload a lease or title doc.\nPaste your Excel headers.\nSubmit special formatting requests.\nUse /balance or /subscribe anytime.")
    elif message_text == "/balance":
        bot.send_message(chat_id=chat_id, text="💳 You currently have $12.00 in processing balance.")
    elif message_text == "/addfunds":
        bot.send_message(chat_id=chat_id, text="To add funds, choose Stripe or BTC:\n[Stripe Link]\n[BTC Wallet Address]")
    elif message_text == "/subscribe":
        bot.send_message(chat_id=chat_id, text="📅 Unlimited plan: $750/month for up to 1,000 documents.\nSubscribe here: [Stripe Plan Link]")
    else:
        bot.send_message(chat_id=chat_id, text="🧾 Got it. If that was a document, we'll process it. Otherwise, please upload your file or paste your column headers.")

    return "ok"

@app.route("/")
def index():
    return "🧠 TitleMindBot is up and running."

if __name__ == "__main__":
    print("🚀 Flask server starting...")
    app.run(port=5000)
