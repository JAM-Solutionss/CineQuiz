import streamlit as st
from backend.modules.css import load_css

# Load custom CSS
st.markdown(load_css(r'frontend/styles.css'), unsafe_allow_html=True)

st.title("What is CineBrowse?")
st.write("CineBrowse is a movie quiz, where you can test your knowledge on movies and their details.")
st.subheader("Our Team:")
st.markdown(
    """
    <p align="center">
        <a href="https://github.com/cipher-shad0w" target="_blank">Cipher Shadow</a>
        <a href="https://github.com/arvedb" target="_blank">Arved Bahde</a>
        <a href="https://github.com/mirixy" target="_blank">Miriam</a>
    </p>
    """, unsafe_allow_html=True
)