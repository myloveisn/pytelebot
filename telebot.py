from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Command handler for the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I am your simple Telegram bot. How can I assist you?")

# Command handler for the /help command
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("You can use the following commands:\n"
                              "/start - Start the bot\n"
                              "/help - Get help\n"
                              "Just type anything, and I'll echo it back!")

# Message handler to echo back any text message
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"You said: {update.message.text}")

def main():
    # Replace 'YOUR_BOT_TOKEN' with your bot's token from BotFather
    token = 'YOUR_BOT_TOKEN'

    # Create the Updater and pass the bot's token
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add handlers for commands and messages
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the bot
    updater.start_polling()

    print("Bot is running. Press Ctrl+C to stop.")
    updater.idle()  # Run the bot until you manually stop it

if __name__ == '__main__':
    main()
