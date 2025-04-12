import logging
import asyncio
from consts import TOKEN, CHAT_ID
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Turn on logging to see what the bot is doing
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
class TextMessage:
    def __init__(self, text: str):
        self.update = Update
        self.text = text


    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        print(f"CHAT_ID = {chat_id}")  # Print chat_id to console
        await context.bot.send_message(chat_id=chat_id, text=self.text)

    async def send(self, app: ApplicationBuilder):
        await app.bot.send_message(chat_id=CHAT_ID, text=self.text)

# This function sends a message to the user when the bot is started
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    print(f"CHAT_ID = {chat_id}")  # Print chat_id to console
    await context.bot.send_message(chat_id=chat_id, text="✅ Bot is alive and responding!")
# Function to send a file (e.g., a document)
async def send_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Define the path to your file (example: 'path/to/your/file.pdf')
    file_path = 'D:\Job\DecorAuto\TelegramBot\hello.txt'

    # Send the file to the chat
    await context.bot.send_document(chat_id=CHAT_ID, document=open(file_path, 'rb'))

    # Notify the user that the file was sent
    await update.message.reply_text("📂 The file has been sent!")

# Function to send an image
async def send_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Define the path to your image file (example: 'path/to/your/image.jpg')
    image_path = 'D:\Job\DecorAuto\TelegramBot\sun.png'

    # Send the image to the chat
    await context.bot.send_photo(chat_id=CHAT_ID, photo=open(image_path, 'rb'))

    # Notify the user that the image was sent
    await update.message.reply_text("🖼️ The image has been sent!")

# Function to send a message without the need for user interaction
async def send_initial_message(app):
    await app.bot.send_message(chat_id=CHAT_ID, text="✅ Bot has started and is sending messages!")

# Function to send a file (e.g., a document)
async def send_immediate_file(app):
    # Define the path to your file (example: 'path/to/your/file.pdf')
    file_path = 'D:\Job\DecorAuto\TelegramBot\hello.txt'

    # Send the file to the chat
    await app.bot.send_document(chat_id=CHAT_ID, document=open(file_path, 'rb'))

    # Notify that the file was sent
    print("File sent successfully!")  # Optionally log to the console

# Function to send an image
async def send_immediate_image(app):
    # Define the path to your image file (example: 'path/to/your/image.jpg')
    image_path = 'D:\Job\DecorAuto\TelegramBot\sun.png'

    # Send the image to the chat
    await app.bot.send_photo(chat_id=CHAT_ID, photo=open(image_path, 'rb'))

    # Notify that the image was sent
    print("Image sent successfully!")  # Optionally log to the console

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Start the bot
    app.add_handler(CommandHandler("start", TextMessage("✅ Bot is alive and responding!").start))
    app.add_handler(CommandHandler("send_file", send_file))
    app.add_handler(CommandHandler("send_image", send_image))

    # Use the event loop to create the initial message task
    loop = asyncio.get_event_loop()
    loop.create_task(send_initial_message(app))  # Run the function when the bot starts
    loop.create_task(send_immediate_file(app))  # Run the function when the bot starts
    loop.create_task(send_immediate_image(app))  # Run the function when the bot starts

    # Run polling
    app.run_polling()

if __name__ == '__main__':
    main()
