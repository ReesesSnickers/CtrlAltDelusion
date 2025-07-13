import os
from openai import OpenAI

def generate_response(origional_response):
    client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
    # prompt = f"Replace any {{{{mood: value}}}} by replacing the {{{{mood: value}}}} with a response that is based on the mood an the value: \n\"{origional_response}\"\n"

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

    return new_response