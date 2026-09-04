from __future__ import annotations

import re

from src.models import ExtractedIntent


def _parse_budget(query: str) -> tuple[float | None, float | None]:
    match = re.search(r"(?:under|below|upto|up to|within|budget)\s*₹?\s*(\d+(?:,\d{3})*(?:\.\d+)?)(k|000)?", query, re.I)
    if match:
        value = float(match.group(1).replace(",", ""))
        if match.group(2):
            value *= 1000
        return None, value

    ranges = re.findall(r"₹?\s*(\d+(?:,\d{3})*(?:\.\d+)?)(k|000)?\s*(?:to|-)\s*₹?\s*(\d+(?:,\d{3})*(?:\.\d+)?)(k|000)?", query, re.I)
    if ranges:
        low_value, low_scale, high_value, high_scale = ranges[0]
        low = float(low_value.replace(",", "")) * (1000 if low_scale else 1)
        high = float(high_value.replace(",", "")) * (1000 if high_scale else 1)
        return low, high

    price_match = re.search(r"₹?\s*(\d+(?:,\d{3})*(?:\.\d+)?)(k|000)?", query, re.I)
    if price_match:
        value = float(price_match.group(1).replace(",", ""))
        if price_match.group(2):
            value *= 1000
        return None, value
    return None, None


def _parse_weight(query: str) -> float | None:
    match = re.search(r"(?:weight|lightweight|portable|not too heavy)\s*(?:under|below|less than|upto|up to)?\s*(\d+(?:\.\d+)?)\s*(?:kg|kilograms?)", query, re.I)
    if match:
        return float(match.group(1))

    if any(term in query for term in ["lightweight", "portable", "not too heavy", "easy to carry"]):
        return 1.5
    return None


def extract_intent(query: str) -> ExtractedIntent:
    q = query.lower()
    budget_min, budget_max = _parse_budget(q)
    weight_max = _parse_weight(q)

    use_cases = []
    for keyword in ["coding", "gaming", "travel", "student", "content creation", "office", "multimedia"]:
        if keyword.lower() in q:
            use_cases.append(keyword.lower())

    soft_preferences = []
    if "battery" in q or "backup" in q:
        soft_preferences.append("good battery life")
    if "lightweight" in q or "portable" in q or "not too heavy" in q:
        soft_preferences.append("lightweight and portable")
    if "premium" in q:
        soft_preferences.append("premium build quality")
    if "cheap" in q or "budget" in q:
        soft_preferences.append("value for money")
    if "gaming" in q:
        soft_preferences.append("strong graphics performance")

    hard_specs = {}
    if "rtx" in q or "graphics" in q:
        hard_specs["gpu"] = "RTX"
    if "ram" in q:
        hard_specs["ram_gb"] = 16
    if "ssd" in q:
        hard_specs["storage_gb"] = 512

    if not soft_preferences:
        soft_preferences = ["balanced everyday performance"]

    return ExtractedIntent(
        budget_min=budget_min,
        budget_max=budget_max,
        weight_max=weight_max,
        use_cases=use_cases,
        hard_specs=hard_specs,
        soft_preferences=soft_preferences,
    )
