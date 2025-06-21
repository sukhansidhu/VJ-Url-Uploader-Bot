import os
import logging
from config import Config
from pyrogram import Client as Tech_VJ
import asyncio

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Ensure download directory exists
if not os.path.isdir(Config.TECH_VJ_DOWNLOAD_LOCATION):
    os.makedirs(Config.TECH_VJ_DOWNLOAD_LOCATION)

plugins = dict(root="plugins")

# Define both bots
bot1 = Tech_VJ(
    name="bot1",
    bot_token=Config.TECH_VJ_BOT_TOKEN1,
    api_id=Config.TECH_VJ_API_ID,
    api_hash=Config.TECH_VJ_API_HASH,
    plugins=plugins
)

bot2 = Tech_VJ(
    name="bot2",
    bot_token=Config.TECH_VJ_BOT_TOKEN2,
    api_id=Config.TECH_VJ_API_ID,
    api_hash=Config.TECH_VJ_API_HASH,
    plugins=plugins
)

# Async main to run both bots
async def main():
    await bot1.start()
    await bot2.start()
    logger.info("Both bots started successfully.")
    await asyncio.get_event_loop().create_future()  # Keeps the program running

if __name__ == "__main__":
    asyncio.run(main())
