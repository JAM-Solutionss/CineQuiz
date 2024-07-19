import streamlit as st

@st.experimental_dialog("More about the movie")
def movie_popup(data):
    for key, value in data.items():
        st.write(f"{key}: {value}")
    
    