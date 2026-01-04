import streamlit as st
import pandas as pd
from pathlib import Path
import math
import time

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
    background-color: #f6f8fc;
}

/* HEADER */
.sticky-header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 64px;
    background: linear-gradient(90deg, #1e3c72, #2a5298);
    z-index: 999999;
    display: flex;
    align-items: center;
    justify-content: center;
}

.logo {
    position: absolute;
    left: 24px;
    height: 40px;
}

.header-title {
    font-size: 22px;
    color: white;
    font-weight: 700;
}

.page-spacer {
    height: 64px;
}

            
/* BOOK CARD */
.book-card {
    background: white;
    border-radius: 14px;
    padding: 10px;
    height: 320px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
    text-align: center;
}

.book-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 26px rgba(0,0,0,0.18);
}

.book-img {
    height: 150px;
    object-fit: contain;
    margin-bottom: 6px;
}

/* TITLE */
.book-title {
    font-size: 16px;
    font-weight: 700;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.book-author {
    font-size: 14px;
    color: #444;
}

.book-meta {
    font-size: 12px;
    color: #777;
}

.rating {
    color: #f4b400;
    font-weight: 600;
    margin-top: 4px;
}

/* PAGINATION */
.pagination {
    position: fixed;
    bottom: 45px;
    width: 100%;
    background: #f6f8fc;
    padding: 8px;
    text-align: center;
}

/* FOOTER */
.footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    left:0;
    background: linear-gradient(90deg, #1e3c72, #2a5298);
    color: white;
    text-align: center;
    padding: 6px;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown("""
<div class="sticky-header">
    <img class="logo" src="https://shorturl.at/2WRRq">
    <div class="header-title">Clustering Global Development</div>
</div>
<div class="page-spacer"></div>
""", unsafe_allow_html=True)



# ------------------ DATA LOADING ------------------
DATA_DIR = Path(__file__).parent

@st.cache_data(show_spinner=False)
def load_data():
    WorldDeveMeasurement = pd.read_csv(DATA_DIR / "World_development_mesurement.csv", encoding="latin-1")
    return WorldDeveMeasurement

with st.spinner("✨ Loading WorldDeveMeasurement..."):
    WorldDeveMeasurement = load_data()
    st.write(WorldDeveMeasurement.head())




# ------------------ FOOTER ------------------
st.markdown("""
<div class="footer">
© 2026 Book Recommendation System | Built with ❤️ using Streamlit
</div>
""", unsafe_allow_html=True)
