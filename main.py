import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from authorities import TOKEN, CHAT_ID
from configs import TEST_IMG_PATH, TEST_FILE_PATH
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

class ImgMessage:
    def __init__(self, img_path:str = TEST_IMG_PATH):
        self.img_path = img_path
    
    # Function to send an image after receiving a command from bot 
    async def send_image_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):

        # Send the image to the chat
        await context.bot.send_photo(chat_id=CHAT_ID, photo=open(self.img_path, 'rb'))

        # Notify the user that the image was sent
        await update.message.reply_text("🖼️ The image has been sent!")
    
    # Function to send an image
    async def send_image(self, app):
        # Send the image to the chat
        await app.bot.send_photo(chat_id=CHAT_ID, photo=open(self.img_path, 'rb'))


class FileMessage:
    def __init__(self, file_path:str = TEST_FILE_PATH):
        self.file_path = file_path
    
    # Function to send a file (e.g., a document) after Bot command 
    async def send_file_cmd(self, update: Update, context: ContextTypes.DEFAULT_TYPE):

        # Send the file to the chat
        await context.bot.send_document(chat_id=CHAT_ID, document=open(self.file_path, 'rb'))

        # Notify the user that the file was sent
        await update.message.reply_text("📂 The file has been sent!")
    
    # Function to send a file (e.g., a document) without Bot command
    async def send_file(self, app):

        # Send the file to the chat
        await app.bot.send_document(chat_id=CHAT_ID, document=open(self.file_path, 'rb'))

        # Notify that the file was sent
        logging.log(level=logging.DEBUG, msg="File sent successfully!")  # Optionally log to the console

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Start the bot
    app.add_handler(CommandHandler("start", TextMessage("✅ Bot is alive and responding!").start))
    app.add_handler(CommandHandler("send_image", ImgMessage().send_image_cmd))
    app.add_handler(CommandHandler("send_file", FileMessage().send_file_cmd))

    # Use the event loop to create the initial message task
    loop = asyncio.get_event_loop()
    loop.create_task(TextMessage("✅ Bot has started and is sending messages!").send(app))  # Run the function when the bot starts
    loop.create_task(FileMessage().send_file(app))  # Run the function when the bot starts
    loop.create_task(ImgMessage().send_image(app))  # Run the function when the bot starts

    # Run polling
    app.run_polling()

if __name__ == '__main__':
    main()
