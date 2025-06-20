pip install -r requirements.txt
from zodiac import get_zodiac_sign
from retriever import retrieve_chunks
from prompt_builder import build_prompt
from ollama_client import call_ollama

def get_insight(name, birth_date, birth_time, birth_place):
    zodiac = get_zodiac_sign(birth_date)
    birth_info = f"{birth_date} {birth_time}, {birth_place}"

    chunks = retrieve_chunks(f"daily horoscope for {zodiac}")
    prompt = build_prompt(name, birth_info, zodiac, chunks)
    
    insight = call_ollama(prompt)
    return {
        "zodiac": zodiac,
        "insight": insight.strip(),
        "language": "en"
    }

if __name__ == "__main__":
    import sys

    name = input("Enter your name: ")
    birth_date = input("Enter birth date (YYYY-MM-DD): ")
    birth_time = input("Enter birth time (HH:MM): ")
    birth_place = input("Enter birth place: ")

    result = get_insight(name, birth_date, birth_time, birth_place)
    print("\n Astrological Insight:")
    print(result)
