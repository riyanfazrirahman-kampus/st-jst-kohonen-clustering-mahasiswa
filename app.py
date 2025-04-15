import streamlit as st

# Tampilan utama
st.set_page_config(page_title="Clustering Mahasiswa", layout="wide")

home_page = st.Page("pages/home.py", title="Home", icon="🏠", default=True)

pg = st.navigation([
    home_page, 
])

pg.run()