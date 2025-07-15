import asyncio
import os
import aiohttp  # ← ADD THIS
import signal
import sys
from dotenv import load_dotenv
from web import app
from bot import bot
from logger import logger

load_dotenv()

async def shutdown():
    logger.info("🧹 Délulu bot is low on energy and is shutting down...")
    await bot.close()

# 🌡️ Keep Render Awake
async def keep_alive():
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://ctrlaltdelusion.onrender.com/health") as resp:
                    logger.info(f"🫀 Keep-alive ping responded with status: {resp.status}")
        except Exception as error:
            logger.warning(f"🥶 Délulu ping failed: {error}")
        await asyncio.sleep(780)  # every 13 minutes. Render spools down every 15 minutes for free tier

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
    bot_task = asyncio.create_task(bot.start(discord_api_key))
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
