from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text):
    prompt = f"Summarize this meeting transcript in bullet points: {text}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    summary = response.choices[0].message.content
    return summary