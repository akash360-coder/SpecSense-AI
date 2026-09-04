from src.intent_extractor import extract_intent
from src.recommender import recommend_products


def test_extract_intent_parses_budget_and_preferences():
    intent = extract_intent("Looking for a lightweight laptop under ₹30k, good for coding and battery backup")
    assert intent.budget_max == 30000
    assert intent.weight_max is not None
    assert "coding" in intent.use_cases
    assert any("battery" in pref.lower() for pref in intent.soft_preferences)


def test_recommend_products_returns_ranked_output():
    results = recommend_products(
        "Budget ₹25k, need a lightweight laptop for coding",
        user_id=None,
        top_n=3,
    )
    assert len(results) > 0
    assert results[0].match_score >= 0
    assert results[0].product_id
