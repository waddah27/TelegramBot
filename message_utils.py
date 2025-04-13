import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes
from authorities import CHAT_ID
from configs import TEST_IMG_PATH, TEST_FILE_PATH

class TextMessage:
    def __init__(self, text: str):
        self.update = Update
        self.text = text

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """message to be sent when commanding /start in the Bot"""
        chat_id = update.effective_chat.id
        print(f"CHAT_ID = {chat_id}")  # Print chat_id to console
        await context.bot.send_message(chat_id=chat_id, text=self.text)

    async def send(self, app: ApplicationBuilder):
        """message to be sent automatically without commands from Bot"""
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