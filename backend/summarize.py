from openai import OpenAI

client = OpenAI(api_key="your-api-key-here")

def summarize_text(text):
    prompt = f"Summarize this meeting transcript in bullet points:\n\n{text}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    summary = response.choices[0].message.content
    return summary
