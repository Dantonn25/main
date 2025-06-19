def build_prompt(name, birth_info, zodiac, chunks):
    context = "\n".join([chunk for chunk, _ in chunks])
    prompt = f"""
You are a Vedic astrologer generating personalized advice.

User: {name}
DOB Info: {birth_info}
Zodiac: {zodiac}

Astrological Context:
{context}

Insight:
"""
    return prompt
