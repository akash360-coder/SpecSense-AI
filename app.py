from __future__ import annotations

import streamlit as st

from src.recommender import recommend_products


st.set_page_config(page_title="SpecSense AI", page_icon="🧠", layout="wide")

st.title("SpecSense AI")
st.subheader("Generative product recommendation system")

query = st.text_input(
    "Describe what you want to buy",
    value="Looking for a lightweight laptop under ₹30k, good for coding and battery backup",
)

if st.button("Get Recommendations"):
    with st.spinner("Analyzing your preferences..."):
        results = recommend_products(query, top_n=5)

    if not results:
        st.warning("No product matches were found. Try broadening the search filters.")
    else:
        for result in results:
            with st.container():
                st.markdown(f"### {result.product_name} — ₹{result.price:,.0f}")
                st.progress(min(result.match_score / 100, 1.0))
                st.caption(f"Match score: {result.match_score:.1f}%")
                st.write(result.explanation)
                st.write("**Hard matches:**", result.hard_matches)
                st.write("**Soft matches:**", result.soft_matches)
                if result.trade_offs:
                    st.write("**Trade-offs:**", ", ".join(result.trade_offs))
                st.write("**Availability:**", result.availability)
                st.markdown("---")
