from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = "7690505632:AAEvqGBrgg63BKJZJgimhVUEScfMrdRadTw"
ADMIN_CHAT_ID = 6223202884

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Type your message below 👇")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    msg = update.message.text

    await update.message.reply_text("Submitted ✅")
    await context.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=f"📩 Message from @{user.username or 'Unknown'} ({user.id}):\n\n{msg}"
    )

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = int(context.args[0])
        msg = " ".join(context.args[1:])
        await context.bot.send_message(chat_id=user_id, text=msg)
        await update.message.reply_text("✅ Sent!")
    except:
        await update.message.reply_text("❌ Usage: /reply <user_id> <message>")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("reply", reply))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
