def generate_response(mood, seed):
    # Simple example: tailor reply based on mood
    mood = mood.lower()

    responses = {
        "sad": f"That's darker than my soul on a Monday.",
        "awkward": f"That was so uncomfortable my CPU flinched.",
        "existential": f"Who are we even talking to?",
        "funny": f"Classic. You belong in a meme museum.",
        "angry": f"Let's punch a toaster.",
        "neutral": f"Just vibing, I guess.",
    }

    return responses.get(mood, f"I don’t know how I feel about that... which is on-brand.")