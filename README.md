# Product Recommendation System

A lightweight and explainable product recommendation system built with **Python and Streamlit**. The application interprets natural-language shopping queries, identifies key requirements such as budget, weight, and use case, and ranks products using a combination of rule-based filtering and heuristic matching.

The system also provides clear explanations for recommendations, helping users understand why a product was selected and the trade-offs involved.

---

## 🚀 Key Features

- **Natural-Language Query Processing**
  - Extracts shopping requirements from user queries.
  - Identifies parameters such as budget, weight, product category, and intended use.

- **Rule-Based Product Filtering**
  - Applies hard filters to remove products that do not meet essential requirements.
  - Uses soft matching to rank products based on additional preferences.

- **Explainable Recommendations**
  - Provides reasons behind each recommendation.
  - Highlights important matches and trade-offs between products.

- **Sample Product Catalog**
  - Includes a sample product dataset for testing and demonstration.

- **Review Data Integration**
  - Uses product review information as part of the recommendation workflow.

- **Interactive Streamlit Interface**
  - Simple web interface for entering natural-language shopping requirements and viewing recommendations.

- **Graceful Fallbacks**
  - The application can run without external API services using its built-in recommendation logic.

---

## 🏗️ System Workflow

```text
User Shopping Query
        ↓
Natural-Language Input Processing
        ↓
Requirement Extraction
        ↓
Budget / Weight / Use-Case Identification
        ↓
Hard Filtering
        ↓
Soft Product Matching
        ↓
Product Ranking
        ↓
Explainable Recommendations