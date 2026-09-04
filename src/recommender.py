from __future__ import annotations

from src.data_loader import load_products
from src.intent_extractor import extract_intent
from src.matching_engine import score_product
from src.models import RecommendationResult


def recommend_products(query: str, user_id: str | None = None, top_n: int = 5) -> list[RecommendationResult]:
    intent = extract_intent(query)
    products = load_products()

    scored = []
    for product in products:
        match_score, hard_matches, soft_matches, trade_offs = score_product(product, intent)
        explanation = (
            f"This model fits the request because it meets the core constraints "
            f"with {len(soft_matches)} matching preference signals."
        )
        if intent.budget_max and product.price > intent.budget_max:
            explanation = "This product falls outside the stated budget, so it is ranked lower."

        scored.append(
            RecommendationResult(
                product_id=product.product_id,
                product_name=product.name,
                match_score=match_score,
                hard_matches=hard_matches,
                soft_matches=soft_matches,
                trade_offs=trade_offs,
                unmet_needs=[],
                explanation=explanation,
                price=product.price,
                availability=product.availability,
            )
        )

    scored.sort(key=lambda item: item.match_score, reverse=True)
    return scored[:top_n]
