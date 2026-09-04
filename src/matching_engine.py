from __future__ import annotations

from src.models import Product


def score_product(product: Product, intent) -> tuple[float, dict, dict, list]:
    hard_matches = {}
    soft_matches = {}
    trade_offs = []
    unmet = []

    if intent.budget_max is not None and product.price <= intent.budget_max:
        hard_matches["budget"] = True
    else:
        hard_matches["budget"] = False

    if intent.weight_max is not None and product.weight_kg is not None and product.weight_kg <= intent.weight_max:
        hard_matches["weight"] = True
    elif intent.weight_max is not None:
        hard_matches["weight"] = False

    for use_case in intent.use_cases:
        if use_case == "coding":
            performance = product.ram_gb or 0
            if performance >= 8:
                soft_matches["coding"] = f"{product.name} has {product.ram_gb}GB RAM and suitable performance for coding."
            else:
                unmet.append("coding performance")
        if use_case == "gaming":
            if product.gpu and "rtx" in product.gpu.lower():
                soft_matches["gaming"] = "Dedicated RTX class graphics support."
            else:
                unmet.append("gaming graphics")
        if use_case == "travel":
            if product.weight_kg is not None and product.weight_kg <= 1.5:
                soft_matches["travel"] = "Light enough for travel."
            else:
                unmet.append("travel portability")

    if "good battery life" in intent.soft_preferences:
        if product.battery_life_hours is not None and product.battery_life_hours >= 8:
            soft_matches["battery"] = f"Battery life of {product.battery_life_hours} hours."
        else:
            trade_offs.append("battery life is modest")

    if "lightweight and portable" in intent.soft_preferences:
        if product.weight_kg is not None and product.weight_kg <= 1.5:
            soft_matches["portability"] = f"Weight {product.weight_kg}kg keeps it portable."
        else:
            trade_offs.append("not the lightest option")

    total_score = 0.0
    if hard_matches.get("budget") is True:
        total_score += 0.5
    if hard_matches.get("weight") is True:
        total_score += 0.3
    total_score += min(len(soft_matches) * 0.2, 0.8)
    total_score = min(total_score, 1.0)

    return round(total_score * 100, 1), hard_matches, soft_matches, trade_offs + unmet
