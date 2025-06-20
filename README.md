# 🔮 Astrological Insight Generator

A modular Python-based service that delivers short, personalized daily horoscope insights based on user birth information, zodiac sign, and contextual knowledge retrieved from an external astrological resource.

---

## ✨ Features

- Zodiac sign inference from date of birth  
- Natural-language generation of personalized insights using LLMs  
- RAG (Retrieval-Augmented Generation): contextual grounding via FAISS and external documents  
- CLI and optional Gradio UI for interaction  
- Easy to extend with multilingual support, Panchang data, or LangChain

---

## 🧠 Methodology

### 1. **User Input**

```json
{
  "name": "Ritika",
  "birth_date": "1995-08-20",
  "birth_time": "14:30",
  "birth_place": "Jaipur, India"
}
```

## 2.Zodiac Calculation
We infer the zodiac using static date ranges (e.g., Leo = July 23 – August 22) based on birth_date.

## 3. External Knowledge Base (RAG)
An astrology e-book (converted from PDF) is split into semantic chunks.

Using the sentence-transformers model and FAISS, we create a vector store.

At runtime, relevant chunks are retrieved based on a prompt like "daily horoscope for Leo".

## 4. Prompt Creation
A customized prompt includes:

User name and birth details

Today's date

Inferred zodiac

Retrieved context from the vector store

##5. LLM Generation
The prompt is passed to an LLM (via call_ollama function), which returns a short, structured prediction in valid JSON format.

## Folder Structure 
├── main.py                  # CLI + Gradio interface logic
├── zodiac.py                # Zodiac sign logic
├── retriever.py             # FAISS-based RAG logic
├── prompt_builder.py        # Structured prompt generator
├── ollama_client.py         # LLM call abstraction
├── build_vector_store.py    # Builds FAISS store from text
├── vector_store.pkl         # Pre-built index, chunks, and metadata
├── Astrology-e-book.pdf     # Source data (external)
├── requirements.txt
└── README.md
## CLI Interface
1)pip install -r requirements.txt

2)python main.py

##Sample Output
Jason
{
  "zodiac": "Leo",
  "insight": "Ritika, your natural charisma draws others to you today. Lead with courage and warmth.",
  "language": "en"
}

## Tech Stack
Python 3.10+

FAISS — semantic vector search

sentence-transformers — chunk embedding

Ollama / OpenAI — LLM inference

Gradio — UI

LangChain (optional) — future orchestration

## Future Scope
🌐 Multilingual support with IndicTrans2 or NLLB

📅 Panchang API integration

🧠 User-based personalization (e.g., recurring logins or cached traits)

⚙️ LangChain-based modular LLM pipeline (prompt templates, retrievers, chains)

## External Resources
Astrology-e-book.pdf: downloaded astrology book used to ground insights via RAG

Used to build the vector store with sentence-transformers and FAISS
