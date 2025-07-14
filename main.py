import asyncio
import os
from dotenv import load_dotenv
from web import app
from bot import bot
from logger import logger
import signal
import sys

load_dotenv()

async def shutdown():
    logger.info("🧹 Délulu bot is low on energy and is shutting down...")
    await bot.close()  # Disconnect bot

async def run_all():
    loop = asyncio.get_running_loop()

    # Setup signal handlers (Unix only)
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, lambda: asyncio.create_task(shutdown()))
        except NotImplementedError:
            logger.warning(f"⚠️ Signal handling not supported on this platform for {sig}")
    
    # Start Quart and bot
    logger.info("📡 Starting Quart server and Discord bot")
    logger.info('☕️ Brewing coffee and nudging Délulu bot awake')
    app_task = asyncio.create_task(app.run_task(host="0.0.0.0", port=5000))
    logger.info('💭 Délulu bot is contiplating life choices')
    discord_api_key = os.getenv("DISCORD_BOT_TOKEN")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not discord_api_key or not openai_api_key:
        raise EnvironmentError("Missing DISCORD_BOT_TOKEN or OPENAI_API_KEY")
    logger.info('🌋 Délulu bot is having a melt down in the bed')
    bot_task = asyncio.create_task(bot.start(os.getenv("DISCORD_BOT_TOKEN")))
    logger.info('💭 Délulu bot is making its decision...')
    # Wait for either to finish
    done, pending = await asyncio.wait(
        [app_task, bot_task],
        return_when=asyncio.FIRST_COMPLETED
    )

    # Cancel remaining tasks
    for task in pending:
        task.cancel()

if __name__ == "__main__":
    try:
        asyncio.run(run_all())
    except KeyboardInterrupt:
        logger.info("🛑 Ctrl+C detected outside loop — exiting.")
    except Exception as error:
        logger.critical(f"🛌 Délulu bot doesn't want to get out of bed today: {error}", exc_info=True)

