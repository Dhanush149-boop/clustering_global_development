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
.block-container {
    padding-top: 0rem !important;
}
header, footer {
    visibility: hidden;
    height: 0;
}
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
    left:0;
    display: flex;
    align-items: center;
    justify-content: center;
}

.header-title {
    font-size: 22px;
    color: white;
    font-weight: 700;
}

.page-spacer {
    height: 70px;
}

/* CARD */
.card {
    background: white;
    border-radius: 14px;
    padding: 18px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    text-align: center;
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 28px rgba(0,0,0,0.16);
}

.card-title {
    font-size: 17px;
    font-weight: 700;
    margin-bottom: 6px;
}

.card-sub {
    font-size: 13px;
    color: #666;
}

/* FOOTER */
.footer {
    position: fixed;
    bottom: 0;
    left:0;
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

# ------------------ DATA LOADING ------------------
DATA_DIR = Path(__file__).parent

@st.cache_data(show_spinner=False)
def load_data():
    return pd.read_csv(
        DATA_DIR / "World_development_mesurement.csv",
        encoding="latin-1"
    )

with st.spinner("✨ Loading World Development Data..."):
    df = load_data()

# ------------------ MAIN CONTENT ------------------
st.subheader("📊 Country Development Overview")

# Country selection
countries = sorted(df["Country"].unique())
selected_country = st.selectbox("🌐 Select a Country", countries)

country_data = df[df["Country"] == selected_country].iloc[0]

# ------------------ DATA CARDS ------------------
cols = st.columns(4)

for i, (col, value) in enumerate(country_data.items()):
    if col == "Country":
        continue
    with cols[i % 4]:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">{col}</div>
            <div class="card-sub">{value}</div>
        </div>
        """, unsafe_allow_html=True)

# ------------------ RAW DATA PREVIEW ------------------
with st.expander("📄 View Raw Dataset"):
    st.dataframe(df, use_container_width=True)

# ------------------ FOOTER ------------------
st.markdown("""
<div class="footer">
© 2026 Clustering Global Development | Built with ❤️ using Streamlit
</div>
""", unsafe_allow_html=True)
