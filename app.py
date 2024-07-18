import streamlit as st
from backend.modules.css import load_css



# Pages
home = st.Page(
    "frontend/webpages/home.py",
    title="Home",
    icon=":material/home:"
)

about = st.Page(
    "frontend/webpages/about.py",
    title="About",
    icon=":material/info:"
)

# Navigation
pg = st.navigation({"Menu": [home, about]})

pg.run()