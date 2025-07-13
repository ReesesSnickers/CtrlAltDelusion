import discord
import re
import os
from discord.ext import commands
from dotenv import load_dotenv
from mood_engine import detect_mood
from response_engine import generate_response

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    # Do nothing if the message came from the bot or if the message came from a bot.
    if message.author.bot:
        return

    #  Find all instances of {{variable}} and create a array
    matches = re.findall(r"\{\{(.*?)\}\}", message.content)
    
    # Loop through the array, determine the mood of the variable then update the {{variable}} to include the mood
    if matches:
        for seed in matches:
            mood = detect_mood(seed)
            match = f"{{{{{seed}}}}}" 
            replacement = f"{{{{{mood}: {seed}}}}}"
            message.content = message.content.replace(match, replacement)

        # Pass the newly formatted string to the openAI response engine to create a new response based on the whole message and variables with moods.
        response = generate_response(message.content)

        await message.channel.send(response)


    # Process the message to the Discord channel
    await bot.process_commands(message)

bot.run(os.getenv("DISCORD_BOT_TOKEN"))