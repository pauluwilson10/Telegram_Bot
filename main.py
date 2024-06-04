from typing import Final
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

TOKEN: Final = "7347339915:AAEqoeIeJTBf7-TwEpX_LF6_tRHvixoo_nU"
BOT_USERNAME: Final = "@fraudude_bot"

# Create inline buttons
button1 = InlineKeyboardButton(text="Juices", callback_data="In_First_button")
button2 = InlineKeyboardButton(text="Diseases", callback_data="In_Second_button")
keyboard_inline = InlineKeyboardMarkup([[button1, button2]])

# Define details for each juice
juice_details = {
    "Carrot": "Carrot juice is a good source of beta carotene, vitamin A, vitamin C, and potassium.",
    "Orange": "Orange juice is high in antioxidants and micronutrients like vitamin C, folate, and potassium.",
    "Dates": "Date juice is rich in essential nutrients like fiber, potassium, and magnesium.",
    "Kiwi": "Kiwi juice is packed with vitamin C, vitamin K, vitamin E, folate, and potassium.",
    "Fig": "Fig juice contains dietary fiber, vitamin B6, copper, potassium, and manganese."
}

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! Thanks for chatting with me...",
        reply_markup=keyboard_inline  # Add the keyboard markup here
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("How can I help you?")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command")

# Callback Query Handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Acknowledge the callback query
    
    if query.data == "In_First_button":
        # Create buttons for juice options
        juice_buttons = [
            InlineKeyboardButton(text="1. Carrot", callback_data="Juice_Carrot"),
            InlineKeyboardButton(text="2. Orange", callback_data="Juice_Orange"),
            InlineKeyboardButton(text="3. Dates", callback_data="Juice_Dates"),
            InlineKeyboardButton(text="4. Kiwi", callback_data="Juice_Kiwi"),
            InlineKeyboardButton(text="5. Fig", callback_data="Juice_Fig")
        ]
        juice_keyboard = InlineKeyboardMarkup.from_row(juice_buttons)
        await query.edit_message_text(text="What juice are you craving for?", reply_markup=juice_keyboard)
    elif query.data.startswith("Juice_"):
        juice_name = query.data.split("_")[1]
        response_text = juice_details.get(juice_name, "No details available.")
        await query.edit_message_text(text=response_text)
    elif query.data == "In_Second_button":
        response_text = "You pressed Button 2"
        await query.edit_message_text(text=response_text)

# Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if "hello" in processed:
        return "Hey there!!"
    elif "how are you" in processed:
        return "I am good"
    elif "i love python" in processed:
        return "Remember to subscribe!!!"
    elif "who am i" in processed:
        return "Hello, I think it's John there. Nice to meet you!"

    return "I do not understand what you wrote"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print("Bot:", response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

if __name__ == "__main__":
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Callback Query Handler
    app.add_handler(CallbackQueryHandler(button_handler))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print("Polling...")
    app.run_polling(poll_interval=3.0)
