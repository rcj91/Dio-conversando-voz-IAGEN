import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[2]
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH, override=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WHISPER_MODEL = os.getenv("WHISPER_MODEL", "base")
LANGUAGE = os.getenv("LANGUAGE", "pt")

print("ENV_PATH:", ENV_PATH)
print("OPENAI_API_KEY repr:", repr(OPENAI_API_KEY))
print("WHISPER_MODEL repr:", repr(WHISPER_MODEL))
print("LANGUAGE repr:", repr(LANGUAGE))