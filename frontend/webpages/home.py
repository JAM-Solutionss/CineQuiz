import streamlit as st
import json
from backend.modules.random_movie import get_movie
from backend.modules.omdb_api import get_movie_data
import random
import requests
from PIL import Image
from io import BytesIO






if not "quiz_started" in st.session_state:
        st.session_state.quiz_started = False

def get_image_dimensions(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img.size


def checkwinner(winner, user) -> str:
     if user == winner:
          return "Correct Answer"
     else:
          return "Incorrect Answer"

def get_data() -> dict:
    title = generate_title()
    data = get_movie_data(title)
    return data

def generate_title() -> str:
     return get_movie()

def change_state():
     if st.session_state.quiz_started == False:
        st.session_state.quiz_started = True
     else:
        st.session_state.quiz_started = False
        if "quiz_data" in st.session_state:
            del st.session_state.quiz_data

def display_movie_card(data, title_height, image_height):
                with st.container():
                    st.markdown(f"""
                        <div style="
                            padding: 20px;
                            border-radius: 10px;
                            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
                            background-color: #f8f8f8;
                            text-align: center;
                            height: {image_height + title_height + 160}px;
                        ">
                            <h2 style="color: #333; margin-bottom: 15px;">{data.get("Title")}</h2>
                            <img src="{data.get("Poster")}" style="width:100%; max-height: 400px; object-fit: contain; border-radius: 5px; margin-bottom: 15px;">
                            <p style="font-size: 1.1em; color: #666;">{data.get("Year")} | {data.get("Genre")}</p>
                            <p style="font-weight: bold; color: #444;">Metacritic: {data.get("Metascore")}</p>
                        </div>
                        """, unsafe_allow_html=True)

def display_question(winner_movie, answer):
    st.write("Which movie is this?")
    c = st.container()
    c.write(winner_movie.get("Plot"))
    col1, col2, col3 = st.columns([1, 1, 1]) 
    with col1:
        if st.button("Movie 1"):
             st.success(checkwinner(answer, user="data1"))
             change_state() 
    with col2:
        if st.button("Movie 2"):
             st.success(checkwinner(answer, user="data2"))
             change_state()
    with col3:
        if st.button("Movie 3"):
             st.success(checkwinner(answer, user="data3"))
             change_state()
    
    if st.button("Hint:"):
         st.write(f"The Metacritic score is: {winner_movie.get('Metascore')}")
   

def display_quiz():
    if "quiz_data" not in st.session_state:
        st.session_state.quiz_data = {
            "data1": get_data(),
            "data2": get_data(),
            "data3": get_data(),
            "winner_movie": f"data{random.randint(1, 3)}"
        }

    if st.session_state.quiz_started:
        data1 = json.loads(st.session_state.quiz_data["data1"])
        data2 = json.loads(st.session_state.quiz_data["data2"])
        data3 = json.loads(st.session_state.quiz_data["data3"])
        winner_movie = st.session_state.quiz_data["winner_movie"]


        # Calculate image heights
        image_heights = [
            get_image_dimensions(data1.get("Poster"))[1],
            get_image_dimensions(data2.get("Poster"))[1],
            get_image_dimensions(data3.get("Poster"))[1]
        ]
        max_image_height = max(image_heights)

        # Calculate the longest title
        titles = [data1.get("Title"), data2.get("Title"), data3.get("Title")]
        max_title_length = max(len(title) for title in titles)
        
        # Calculate dynamic height (you may need to adjust the multiplier)
        title_height = max(60, max_title_length * 1.5)  # Minimum 60px, or 1.5px per character

        c = st.container()
        col1, col2, col3 = c.columns([1, 1, 1])
        with col1:
            display_movie_card(data1, title_height, max_image_height)
        with col2:
            display_movie_card(data2, title_height, max_image_height)
        with col3:
            display_movie_card(data3, title_height, max_image_height)
        
        st.write(winner_movie)
    
        if winner_movie == "data1":
            data = data1
        elif winner_movie == "data2":
            data = data2
        elif winner_movie == "data3":
            data = data3
        else:
            data = None
        st.divider() 
        display_question(data, winner_movie)
        st.divider()
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

