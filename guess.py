import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
def guess_action(actions):
    prompt = f"""
    You are playing dumb charades.
    Actions: {actions}
    Guess the movie or word in 1-2 words.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content