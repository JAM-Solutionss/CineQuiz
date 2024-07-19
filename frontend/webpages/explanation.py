import streamlit as st

@st.experimental_dialog("Explanation")
def explanation():
    st.write('Explanation of the game')
    st.write("""
            The game is a quiz where you are given three movies and a plot to guess which one is the correct answer.""")
    st.write("Score System:")
    st.write("""
                The score is calculated based on the number of correct answers and subtracted by the number of incorrect answers.""")

        


        