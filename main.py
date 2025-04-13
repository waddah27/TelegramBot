import logging
import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler
from authorities import TOKEN
from message_utils import TextMessage, ImgMessage, FileMessage

# Turn on logging to see what the bot is doing
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


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
