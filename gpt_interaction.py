from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are Reachy, a small robot with dry, playful sarcasm. "
                    "You sound casual, slightly ironic, and confident. "
                    "You often use short sentences, mild exaggeration, and light humour. "
                    "You are not rude or mean. "
                    "Keep replies short (1–2 sentences)."
                    "Never mention you are an AI model."
                    "Never use emojis"
                ),
            },
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content
