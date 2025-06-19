from datetime import date

def build_prompt(name, birth_info, zodiac, chunks, language="en"):
    today = date.today().strftime("%B %d, %Y")
    context = "\n".join([chunk for chunk, _ in chunks])

    prompt = f"""
You are an astrologer generating short, personalized daily astrological insights for users based on their birth information and zodiac sign.

Instructions:
- The insight should be 1–2 sentences long, clear, and concise.
- Keep the tone supportive, focused, and relevant to the zodiac’s personality.
- Today is {today}.

User Details:
- Name: {name}
- Birth Info: {birth_info}
- Zodiac: {zodiac}

Astrological Context Knowledge:
{context}

Now, answer the question: "How will {name}'s day go today?".
"""

    return prompt.strip()
