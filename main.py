from typing import Final
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

TOKEN: Final = "7347339915:AAEqoeIeJTBf7-TwEpX_LF6_tRHvixoo_nU"
BOT_USERNAME: Final = "@fraudude_bot"

# Create inline buttons
button1 = InlineKeyboardButton(text="Juices", callback_data="In_First_button")
button2 = InlineKeyboardButton(text="Food", callback_data="In_Second_button")
keyboard_inline = InlineKeyboardMarkup([[button1, button2]])

# Define details for each juice
juice_details = {
  "Carrot": "**Carrot juice** is a good source of beta carotene, vitamin A, vitamin C, and potassium.\n\n(As per 100ml)\nCalories: 41\nProtein: 0.6 grams\nFat: Less than 0.2 grams",
  "Orange": "**Orange juice** is high in antioxidants and micronutrients like vitamin C, folate, and potassium.\n\n(As per 100ml)\nCalories: 44\nProtein: 0.8 grams\nFat: Less than 0.2 grams",
  "Dates": "**Date juice** is rich in essential nutrients like fiber, potassium, and magnesium.\n\n(As per 100ml)\nCalories: 282\nProtein: 0.2 grams\nFat: Less than 0.2 grams",
  "Kiwi": "**Kiwi juice** is packed with vitamin C, vitamin K, vitamin E, folate, and potassium.\n\n(As per 100ml)\nCalories: 61\nProtein: 1.1 grams\nFat: Less than 0.2 grams",
  "Fig": "**Fig juice** contains dietary fiber, vitamin B6, copper, potassium, and manganese.\n\n(As per 100ml)\nCalories: 55\nProtein: 0.4 grams\nFat: Less than 0.2 grams",
  "Banana": "**Banana juice** is a good source of potassium, vitamin C, and vitamin B6.\n\n(As per 100ml)\nCalories: 89\nProtein: 1.1 grams\nFat: Less than 0.3 grams",
  "Apple": "**Apple juice** is rich in vitamin C, antioxidants, and dietary fiber.\n\n(As per 100ml)\nCalories: 46\nProtein: 0.1 grams\nFat: Less than 0.1 grams",
  "Blueberry": "**Blueberry juice** is high in antioxidants, vitamin C, and vitamin K.\n\n(As per 100ml)\nCalories: 49\nProtein: 0.4 grams\nFat: Less than 0.1 grams",
  "Guava": "**Guava juice** is a good source of vitamin C, vitamin A, and dietary fiber.\n\n(As per 100ml)\nCalories: 38\nProtein: 0.9 grams\nFat: Less than 0.1 grams",
  "Mango": "**Mango juice** is rich in vitamin C, vitamin A, and antioxidants.\n\n(As per 100ml)\nCalories: 60\nProtein: 0.6 grams\nFat: Less than 0.4 grams"
}
# Define details for each food
nutritional_details = {
    "Almonds": "**Almonds** are rich in healthy fats, fiber, protein, magnesium, and vitamin E.\n\n(As per 100 grams)\nCalories: 576\nProtein: 21.2 grams\nFat: 49.9 grams",
    "Brazil nuts": "**Brazil nuts** are high in selenium, a mineral important for thyroid function and overall health.\n\n(As per 100 grams)\nCalories: 656\nProtein: 14.3 grams\nFat: 66.4 grams",
    "Lentils": "**Lentils** are a great source of plant-based protein, fiber, folate, and iron.\n\n(As per 100 grams)\nCalories: 116\nProtein: 9.0 grams\nFat: 0.4 grams",
    "Oatmeal": "**Oatmeal** is high in fiber, manganese, phosphorus, magnesium, and vitamins B1 and B5.\n\n(As per 100 grams)\nCalories: 389\nProtein: 16.9 grams\nFat: 6.9 grams",
    "Wheat germ": "**Wheat germ** is a concentrated source of nutrients, including vitamin E, folate, phosphorus, thiamine, and magnesium.\n\n(As per 100 grams)\nCalories: 360\nProtein: 23.2 grams\nFat: 9.7 grams",
    "Broccoli": "**Broccoli** is packed with vitamins, minerals, fiber, and antioxidants.\n\n(As per 100 grams)\nCalories: 34\nProtein: 2.8 grams\nFat: 0.4 grams",
    "Apples": "**Apples** are a good source of fiber, vitamin C, and various antioxidants.\n\n(As per 100 grams)\nCalories: 52\nProtein: 0.3 grams\nFat: 0.2 grams",
    "Kale": "**Kale** is one of the most nutrient-dense foods, rich in vitamins A, C, and K, as well as calcium and iron.\n\n(As per 100 grams)\nCalories: 49\nProtein: 4.3 grams\nFat: 0.9 grams",
    "Blueberries": "**Blueberries** are loaded with antioxidants, fiber, and vitamins C and K.\n\n(As per 100 grams)\nCalories: 57\nProtein: 0.7 grams\nFat: 0.3 grams",
    "Avocados": "**Avocados** are high in healthy fats, fiber, potassium, and vitamins K, C, and E.\n\n(As per 100 grams)\nCalories: 160\nProtein: 2.0 grams\nFat: 14.7 grams",
    "Leafy green vegetables": "**Leafy green vegetables** like spinach, kale, and Swiss chard are packed with vitamins, minerals, and antioxidants.\n\n(As per 100 grams)\nCalories: Varies\nProtein: Varies\nFat: Varies",
    "Sweet potatoes": "**Sweet potatoes** are rich in beta-carotene, vitamins A and C, fiber, and potassium.\n\n(As per 100 grams)\nCalories: 86\nProtein: 1.6 grams\nFat: 0.1 grams",
    "Oily fish": "**Oily fish** like salmon, mackerel, and sardines are excellent sources of omega-3 fatty acids, protein, and various vitamins and minerals.\n\n(As per 100 grams)\nCalories: Varies\nProtein: Varies\nFat: Varies",
    "Chicken": "**Chicken** is a good source of protein, niacin, vitamin B6, phosphorus, and selenium.\n\n(As per 100 grams)\nCalories: 239\nProtein: 27.3 grams\nFat: 14.7 grams",
    "Eggs": "**Eggs** are one of the most nutritious foods, containing high-quality protein, vitamins, minerals, and antioxidants.\n\n(As per 100 grams)\nCalories: 143\nProtein: 13.0 grams\nFat: 9.5 grams"
}


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! Thanks for chatting with me...",
        reply_markup=keyboard_inline  # Add the keyboard markup here    
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Helping is my gene,\nEnter the /start to start")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You deserve this day!Conquer the day my King.... ")

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
            InlineKeyboardButton(text="5. Fig", callback_data="Juice_Fig"),
            InlineKeyboardButton(text="6. Banana", callback_data="Juice_Banana"),
            InlineKeyboardButton(text="7. Apple", callback_data="Juice_Apple"),
            InlineKeyboardButton(text="8. Blueberry", callback_data="Juice_Blueberry"),
            InlineKeyboardButton(text="9. Guava", callback_data="Juice_Guava"),
            InlineKeyboardButton(text="10. Mango", callback_data="Juice_Mango")
        ]
        # Create rows with five buttons each
        rows = [juice_buttons[i:i+4] for i in range(0, len(juice_buttons), 4)]
        juice_keyboard = InlineKeyboardMarkup(rows)
        await query.edit_message_text(text="What juice are you craving for?", reply_markup=juice_keyboard)
    elif query.data.startswith("Juice_"):
        juice_name = query.data.split("_")[1]
        response_text = juice_details.get(juice_name, "No details available.")
        await query.edit_message_text(text=response_text)
    elif query.data == "In_Second_button":
        # Create buttons for food options
        nutritional_buttons = [
            InlineKeyboardButton(text="1. Almonds", callback_data="Nutrition_Almonds"),
            InlineKeyboardButton(text="2. Brazil nuts", callback_data="Nutrition_Brazil_nuts"),
            InlineKeyboardButton(text="3. Lentils", callback_data="Nutrition_Lentils"),
            InlineKeyboardButton(text="4. Oatmeal", callback_data="Nutrition_Oatmeal"),
            InlineKeyboardButton(text="5. Wheat germ", callback_data="Nutrition_Wheat_germ"),
            InlineKeyboardButton(text="6. Broccoli", callback_data="Nutrition_Broccoli"),
            InlineKeyboardButton(text="7. Apples", callback_data="Nutrition_Apples"),
            InlineKeyboardButton(text="8. Kale", callback_data="Nutrition_Kale"),
            InlineKeyboardButton(text="9. Blueberries", callback_data="Nutrition_Blueberries"),
            InlineKeyboardButton(text="10. Avocados", callback_data="Nutrition_Avocados"),
            InlineKeyboardButton(text="11. Leafy green vegetables", callback_data="Nutrition_Leafy_green_vegetables"),
            InlineKeyboardButton(text="12. Sweet potatoes", callback_data="Nutrition_Sweet_potatoes"),
            InlineKeyboardButton(text="13. Oily fish", callback_data="Nutrition_Oily_fish"),
            InlineKeyboardButton(text="14. Chicken", callback_data="Nutrition_Chicken"),
            InlineKeyboardButton(text="15. Eggs", callback_data="Nutrition_Eggs")
        ]
        # Create rows with five buttons each
        rows = [nutritional_buttons[i:i+3] for i in range(0, len(nutritional_buttons), 3)]
        food_keyboard = InlineKeyboardMarkup(rows)
        await query.edit_message_text(text="Master EAT HEALTHY.", reply_markup=food_keyboard)
    elif query.data.startswith("Nutrition_"):
        food_name = query.data.split("_")[1]
        response_text = nutritional_details.get(food_name, "No details available.")
        await query.edit_message_text(text=response_text)


        

# Responses
def handle_response(text: str, username: str) -> str:
    processed: str = text.lower()

    if "hello" in processed or "good morning" in processed or "good afternoon" in processed or "good evening" in processed or "who" in processed:
        if username:
            return f"Hello, {username}!!,how is your day going? "
        else:
            return "Hello there!!"
    if "how are you" in processed:
        return "I am good what about you?"
    if "bad" in processed or "not" in processed:
        return "Stay healthy my king it will be alright!!"
    if "fine" in processed or "ok" in processed or "good" in processed:
        return "i am glad that you are having a great day!!!"
    


    return "I do not understand what you wrote... you cant type /start for healthy food and healthy juice suggestions "
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    username: str = update.message.from_user.username if update.message.from_user.username else ""
    
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text, username)
        else:
            return
    else:
        response: str = handle_response(text, username)

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
    print("**Polling...**")
    app.run_polling(poll_interval=3.0)
