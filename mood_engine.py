import os
from openai import OpenAI

def detect_mood(text):
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

    return mood