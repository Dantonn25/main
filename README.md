# Astrological Insight Generator (LLM + Vector DB)

## Features
- Infers zodiac sign from birthdate,and tell how today will look like.
- Embeds & retrieves relevant insights using vector DB
- Uses Ollama (e.g., Mistral) to generate natural language insights
- Can translate in hindi if require

## Usage
1. Put your astrological data that wiill help model to tell how astrological prediction is done
2. Build the vector store:
```bash
python -c "from embedder import build_vector_store; build_vector_store()"
```
3. Run the main script:
```bash
python main.py
```

## Example Output
```json
{
  "zodiac": "Leo",
  "insight": "Your natural charisma will help you shine in difficult meetings today...",
  "language": "en"
}
```
I have not added any language option here.I also tried having ui using streamlit but I was gaving issue. May be later I will sort that out.
Can you plug in LangChain or a real Panchang API later?: Yes we can. 
