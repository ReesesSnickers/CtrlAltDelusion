import asyncio
import os
import aiohttp
import signal
import ssl
import certifi
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from dotenv import load_dotenv
from src.web import app
from src.bot import bot
from src.bot.logger import logger
from src.bot.bot import start as bot_start

load_dotenv()

async def shutdown():
    logger.info("🧹 Délulu bot is low on energy and is shutting down...")
    await bot.close()

ssl_context = ssl.create_default_context(cafile=certifi.where())

# 🌡️ Keep Render Awake
async def keep_alive():
    app_env = os.getenv('APP_ENV', '')
    app_url = os.getenv('APP_URL', 'https://ctrlaltdelusion.onrender.com')
    sleep_interval = 30 if app_env == 'local' else 780  # every 13 minutes. Render spools down every 15 minutes for free tier in production
    
    # Create single session for entire function
    connector = aiohttp.TCPConnector(ssl=ssl_context)
    session = aiohttp.ClientSession(connector=connector)

    while True:
        try:
            async with session.get(f"{app_url}/health") as resp:
                logger.info(f"🫀 Keep-alive ping responded with status: {resp.status}")
        except Exception as error:
            logger.warning(f"🥶 Délulu ping failed: {error}")
        await asyncio.sleep(sleep_interval)

async def run_all():
    loop = asyncio.get_running_loop()

    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, lambda: asyncio.create_task(shutdown()))
        except NotImplementedError:
            logger.warning(f"⚠️ Signal handling not supported on this platform for {sig}")

    # 🫡 Start Keep-Alive Task
    logger.info("🫡 Délulu ping task engaging: staying emotionally online")
    keep_alive_task = asyncio.create_task(keep_alive())

    # 🔌 Start Quart and Discord bot
    logger.info("📡 Starting Quart server and Discord bot")
    logger.info('☕️ Brewing coffee and nudging Délulu bot awake')
    app_task = asyncio.create_task(app.run_task(host="0.0.0.0", port=5000))
    logger.info('💭 Délulu bot is contemplating life choices')
    discord_api_key = os.getenv("DISCORD_BOT_TOKEN")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not discord_api_key or not openai_api_key:
        raise EnvironmentError("Missing DISCORD_BOT_TOKEN or OPENAI_API_KEY")
    logger.info('🌋 Délulu bot is having a meltdown in the bed')
    bot_task = asyncio.create_task(bot_start(discord_api_key))
    logger.info('💭 Délulu bot is making its decision...')

    done, pending = await asyncio.wait(
        [app_task, bot_task, keep_alive_task],
        return_when=asyncio.FIRST_COMPLETED
    )

    for task in pending:
        task.cancel()

if __name__ == "__main__":
    try:
        asyncio.run(run_all())
    except KeyboardInterrupt:
        logger.info("🛑 Ctrl+C detected outside loop — exiting.")
    except Exception as error:
        logger.critical(f"🛌 Délulu bot doesn't want to get out of bed today: {error}", exc_info=True)