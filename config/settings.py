import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama").lower()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if LLM_PROVIDER == "ollama":
    MODEL_NAME = os.getenv("MODEL_NAME", "gemma3:4b")
    API_KEY = "ollama"
    BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
else:
    MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
    API_KEY = OPENAI_API_KEY
    BASE_URL = None
    if not API_KEY:
        raise ValueError(
            "OPENAI_API_KEY is missing. Check your .env file."
        )

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

MAX_AGENT_ITERATIONS = 5