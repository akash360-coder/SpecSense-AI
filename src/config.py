from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

DATA_DIR = BASE_DIR / "data"
PRODUCTS_PATH = DATA_DIR / "products.csv"
REVIEWS_PATH = DATA_DIR / "reviews.csv"
USER_PROFILES_PATH = DATA_DIR / "user_profiles.csv"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "gemini")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.0-flash")


def get_llm_config() -> dict:
    return {
        "provider": LLM_PROVIDER,
        "model": MODEL_NAME,
        "gemini_api_key": GEMINI_API_KEY,
        "openai_api_key": OPENAI_API_KEY,
    }
