from __future__ import annotations

import pandas as pd

from src.config import PRODUCTS_PATH, REVIEWS_PATH, USER_PROFILES_PATH
from src.models import Product, Review, UserProfile


def load_products() -> list[Product]:
    df = pd.read_csv(PRODUCTS_PATH)
    df = df.copy()
    df["product_id"] = df["product_id"].astype(str)
    return [Product(**row.to_dict()) for _, row in df.iterrows()]


def load_reviews() -> list[Review]:
    df = pd.read_csv(REVIEWS_PATH)
    return [Review(**row.to_dict()) for _, row in df.iterrows()]


def load_user_profiles() -> list[UserProfile]:
    df = pd.read_csv(USER_PROFILES_PATH)
    return [UserProfile(**row.to_dict()) for _, row in df.iterrows()]


def load_catalog() -> tuple[list[Product], list[Review], list[UserProfile]]:
    return load_products(), load_reviews(), load_user_profiles()
