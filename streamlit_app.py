import streamlit as st
import pandas as pd

vehicles = ["Car A", "Car B", "Car C"]
categories = ["Comfort", "Handling", "Technology", "Style"]

if "ratings" not in st.session_state:
    st.session_state.ratings = []

st.title("🚗 Dealer Car Rating Prototype")

st.header("Submit Your Rating")
with st.form("rating_form"):
    selected_vehicle = st.selectbox("Select Vehicle", vehicles)
    ratings = {}
    for category in categories:
        ratings[category] = st.slider(f"{category} Rating", 1, 10, 5)
    submitted = st.form_submit_button("Submit Rating")
    if submitted:
        st.session_state.ratings.append({"Vehicle": selected_vehicle, **ratings})
        st.success("Rating submitted!")

st.header("📊 Live Rating Dashboard")
if st.session_state.ratings:
    df = pd.DataFrame(st.session_state.ratings)
    avg_scores = df.groupby("Vehicle").mean().reset_index()
    st.dataframe(avg_scores.style.format("{:.2f}"))
else:
    st.info("No ratings submitted yet.")
