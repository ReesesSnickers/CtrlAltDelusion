import discord
import re
from discord.ext import commands
from src.bot.mood_engine import detect_mood
from src.bot.response_engine import generate_response
from src.bot.logger import logger

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    logger.info('🌈 - Successfully completed the awakening. Délulu bot is ready for action.')
    logger.debug(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    # Do nothing if the message came from the bot or if the message came from a bot.
    if message.author.bot:
        return

    #  Find all instances of {{variable}} and create a array
    matches = re.findall(r"\{\{(.*?)\}\}", message.content)
    
    # Loop through the array, determine the mood of the variable then update the {{variable}} to include the mood
    if matches:
        new_content = message.content

        for seed in matches:
            mood = detect_mood(seed)
            if mood in ["invalid", "error"]:
                mood = "disgruntled"
                logger.info(f'🗑️ Délulu bot is being lazy and just jotting the mood down as {mood}')
            match = f"{{{{{seed}}}}}"
            replacement = f"{{{{{mood}: {seed}}}}}"
            new_content = new_content.replace(match, replacement)
        
        # Pass the newly formatted string to the openAI response engine to create a new response based on the whole message and variables with moods.
        response = generate_response(new_content)
        logger.info(f"🗣️ Délulu bot is sending: {response}")
        await message.channel.send(response)


    # Process the message to the Discord channel
    await bot.process_commands(message)

async def start(token):
    await bot.start(token)

if __name__ == "__main__":
    print("🛑 Don't run bot.py directly! Use main.py.")