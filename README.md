# SpecSense AI

A lightweight product recommendation system built with Python and Streamlit. It parses natural-language shopping queries, ranks products using heuristic matching, and explains recommendations in plain language.

## Features
- Natural-language intent extraction for budget, weight, and product use-cases
- Rule-based hard filtering and soft matching
- Explainable recommendation results with trade-offs
- Sample product catalog and review data
- Streamlit-based UI

## Setup
1. Create a virtual environment and activate it.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your API keys if you want LLM-backed matching.
4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Running tests
```bash
pytest -q
```

## Sample queries
- Looking for a lightweight laptop under ₹30k, good for coding and battery backup
- Need a gaming laptop, budget ₹60k, must have RTX GPU
- Good laptop for content creation, 4-hour+ battery

## Notes
This version includes graceful fallbacks so the app works even without any external API service.
