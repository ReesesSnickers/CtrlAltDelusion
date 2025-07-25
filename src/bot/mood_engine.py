import os
from openai import OpenAI
from src.bot.logger import logger

def detect_mood(text):
    if not text or not isinstance(text, str):
        logger.warning(f"Invalid input for mood detection: {text}")
        return "invalid"
    
    try:
        logger.info(f'⚙️ Délulu bot is grinding its gears trying to understand emotion of {text}')
        client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
        prompt = f"Analyze the mood of the following message and return only the mood determined:\n\"{text}\"\nMood:"
        response = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
            max_tokens=50
        )
        mood = response.choices[0].message.content

        logger.info(f'✨ Délulu bot has no clue and is going to guess the mood is {mood}')
        return mood
    except Exception as error:
        logger.error(f"⛈️ Délulu bot doesn't understand human emotion today: {error}", exc_info=True)
        return "error"