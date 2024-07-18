import streamlit as st
import json

if not "quiz_started" in st.session_state:
        st.session_state.quiz_started = False

def change_state():
     if st.session_state.quiz_started == False:
        st.session_state.quiz_started = True
     else:
        st.session_state.quiz_started = False

def display_movie_card(data):
                with st.container():
                    st.markdown(f"""
                        <div style="
                            padding: 10px;
                            border-radius: 5px;
                            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
                            transition: 0.3s;
                            width: 100%;
                        ">
                            <h3>{data.get("Title")}</h3>
                            <img src="{data.get("Poster")}" style="width:100%">
                            <p>{data.get("Year")} | {data.get("Genre")} | Metacritic: {data.get("Metascore")}</p>                            <p>{data.get("Plot")}</p>
                        </div>
                    """, unsafe_allow_html=True)       

def display_question():
    st.write("Which movie is this?")
    c = st.container()
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.button("Option 1")
    with col2:
        st.button("Option 2")
    with col3:
        st.button("Option 3")
   

def display_quiz():
    data = json.load(open("backend/modules/dummy_data.json"))
    print(data)
    if st.session_state.quiz_started:
        c = st.container()
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            display_movie_card(data)
        with col2:
            display_movie_card(data)
        with col3:
            display_movie_card(data)
        
        display_question()

        if st.button("End Quiz"):
            change_state()
            st.write("Quiz Ended")
            st.rerun()
            


def home_screen():
    if st.session_state.quiz_started == True:
        st.write("Quiz Started")
        display_quiz()
    else:
        st.write("Quiz Not Started")
        st.button("Start Quiz", on_click=change_state)
        
        


st.set_page_config(layout="wide")
home_screen()

