import streamlit as st
import pandas as pd
from pathlib import Path

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Clustering Global Development",
    layout="wide"
)

# ------------------ REMOVE DEFAULT PADDING ------------------
st.markdown("""
<style>
.block-container { padding-top: 0rem !important; }
header, footer { visibility: hidden; height: 0; }
</style>
""", unsafe_allow_html=True)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
body {
    background-color: #f4f6fb;
    font-family: 'Segoe UI', sans-serif;
}

/* HEADER */
.sticky-header {
    position: fixed;
    top: 0;
    width: 100%;
    height: 64px;
    background: linear-gradient(90deg, #2b5876, #4e4376);
    z-index: 999;
    display: flex;
    align-items: center;
    justify-content: center;
}
.header-title {
    font-size: 22px;
    color: white;
    font-weight: 700;
}
.page-spacer { height: 70px; }

/* COUNTRY CARD */
.country-card {
    background: white;
    border-radius: 14px;
    padding: 14px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    text-align: center;
    cursor: pointer;
    transition: all 0.3s ease;
}
.country-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 28px rgba(0,0,0,0.18);
}
.country-name {
    font-size: 16px;
    font-weight: 700;
    color: #2b5876;
}

/* DETAIL CARD */
.detail-card {
    background: white;
    border-radius: 12px;
    padding: 16px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 14px;
}
.detail-title {
    font-size: 14px;
    font-weight: 700;
}
.detail-value {
    font-size: 13px;
    color: #555;
}

/* FOOTER */
.footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    background: #2b5876;
    color: white;
    text-align: center;
    padding: 8px;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown("""
<div class="sticky-header">
    <div class="header-title">🌍 Clustering Global Development</div>
</div>
<div class="page-spacer"></div>
""", unsafe_allow_html=True)

# ------------------ LOAD DATA ------------------
DATA_DIR = Path(__file__).parent

@st.cache_data
def load_data():
    return pd.read_csv(DATA_DIR / "World_development_mesurement.csv", encoding="latin-1")

df = load_data()

# ------------------ SESSION STATE ------------------
if "selected_country" not in st.session_state:
    st.session_state.selected_country = None

# ------------------ SEARCH ------------------
st.subheader("🔍 Search Country")
search_text = st.text_input("Type country name")

filtered_df = df[df["Country"].str.contains(search_text, case=False, na=False)]

# ------------------ COUNTRY CARDS GRID ------------------
st.subheader("🌐 Countries")

cols = st.columns(5)
for i, country in enumerate(filtered_df["Country"].unique()):
    with cols[i % 5]:
        if st.button(country, key=country):
            st.session_state.selected_country = country

# ------------------ COUNTRY DETAILS ------------------
if st.session_state.selected_country:
    st.divider()
    st.subheader(f"📊 {st.session_state.selected_country} – Full Details")

    country_data = df[df["Country"] == st.session_state.selected_country].iloc[0]

    left, right = st.columns(2)

    for i, (col, val) in enumerate(country_data.items()):
        if col == "Country":
            continue
        target = left if i % 2 == 0 else right
        with target:
            st.markdown(f"""
            <div class="detail-card">
                <div class="detail-title">{col}</div>
                <div class="detail-value">{val}</div>
            </div>
            """, unsafe_allow_html=True)

# ------------------ FOOTER ------------------
st.markdown("""
<div class="footer">
© 2026 Clustering Global Development | Built with ❤️ using Streamlit
</div>
""", unsafe_allow_html=True)
