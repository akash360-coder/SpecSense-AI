from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Product(BaseModel):
    product_id: str
    name: str
    category: str
    price: float
    weight_kg: Optional[float] = None
    battery_life_hours: Optional[float] = None
    ram_gb: Optional[int] = None
    storage_gb: Optional[int] = None
    processor: Optional[str] = None
    gpu: Optional[str] = None
    description: str = ""
    availability: str = "In Stock"


class UserProfile(BaseModel):
    user_id: str
    name: str
    age: Optional[int] = None
    budget: Optional[float] = None
    context_tags: List[str] = Field(default_factory=list)
    product_history: List[str] = Field(default_factory=list)


class Query(BaseModel):
    user_id: Optional[str] = None
    raw_input: str
    timestamp: Optional[str] = None


class ExtractedIntent(BaseModel):
    budget_min: Optional[float] = None
    budget_max: Optional[float] = None
    weight_max: Optional[float] = None
    use_cases: List[str] = Field(default_factory=list)
    hard_specs: Dict[str, Any] = Field(default_factory=dict)
    soft_preferences: List[str] = Field(default_factory=list)


class Review(BaseModel):
    product_id: str
    reviewer_name: str
    review_text: str
    rating: float


class RecommendationResult(BaseModel):
    product_id: str
    product_name: str
    match_score: float
    hard_matches: Dict[str, Any] = Field(default_factory=dict)
    soft_matches: Dict[str, Any] = Field(default_factory=dict)
    trade_offs: List[str] = Field(default_factory=list)
    unmet_needs: List[str] = Field(default_factory=list)
    explanation: str
    price: float
    availability: str = "In Stock"


class RecommendationResponse(BaseModel):
    recommendations: List[RecommendationResult]
    best_alternative: Optional[RecommendationResult] = None
    refinement_suggestions: List[str] = Field(default_factory=list)
