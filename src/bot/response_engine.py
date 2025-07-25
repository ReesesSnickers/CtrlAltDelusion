import os
from openai import OpenAI
from src.bot.logger import logger

def generate_response(origional_response):
    try:
        logger.info(f'🧩 Délulu bot is consulting OpenAi for their thoughts.')
        client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
        prompt = f"Take the following sentence and replace any {{{{mood: content}}}} or {{{{insert ...}}}} tags with a short, creative phrase that matches the mood or intent and the content. Keep the rest of the sentence unchanged.\nExample:\nInput: \"well isn't this just great {{{{insert funny joke}}}}. Would you like a {{{{sad: depressing statement}}}}\"\nOutput: \"Well isn't this just great the fridge is running. Would you like dying cat?\"\nBe playful and surreal with the replacements. Use unexpected dark absurdity.\nNow transform this:\n\"{origional_response}\""
        gpt_response = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
            max_tokens=50
        )

        new_response = gpt_response.choices[0].message.content.strip()
        logger.info(f'💡 Délulu bot has had a lightbulb moment: {new_response}')
        return new_response
    except KeyboardInterrupt:
        logger.info("🛑 Délulu bot received Ctrl+C. Shutting down gracefully.")
    except Exception as error:
        logger.error(f'🫏 Délulu bot is refusing to speak. What did we do this time... {error}', exc_info=True)