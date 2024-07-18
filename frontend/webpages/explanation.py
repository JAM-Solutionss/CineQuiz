import streamlit as st

@st.experimental_dialog("Explanation")
def explanation():
    st.write('Explanation of the game')
    
    if st.Button('Further'):
        st.rerun()