# Astrological Insight Generator (LLM + Vector DB)

## Features
- Infers zodiac sign from birthdate
- Embeds & retrieves relevant insights using vector DB
- Uses Ollama (e.g., Mistral) to generate natural language insights

## Usage
1. Put your astrological data in the `data/` folder (e.g., `leo.txt`, `virgo.txt`)
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
