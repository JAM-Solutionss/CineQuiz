import streamlit as st
import json
from backend.modules.random_movie import get_movie
from backend.modules.omdb_api import get_movie_data
import random
import requests
from PIL import Image
from io import BytesIO


st.set_page_config(layout="wide")
st.title("CineBrowse")
 




def set_button_state(user_answer):
     st.session_state.quiz_data['user_answer'] = user_answer
     

def get_image_dimensions(url):
    if url is None or url == 'N/A':
        return (0, 0)  # Return a default size if no valid URL is provided
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img.size
    except:
        return (0, 0)  # Return default size if there's any error in fetching or processing the image


def checkwinner(winner, user) -> str:
     win = winner
     print(f"winner is : {win}")
     print(f"user_answer is : {user}")
     if user == win:
          return "Correct Answer"
     else:
          return "Incorrect Answer"

def get_data() -> dict:
    title = generate_title()
    data = get_movie_data(title)
    test = json.loads(data)
    if test.get("Title") is None:
        return get_data()  # Retry if title is not found
    return data

def generate_title() -> str:
     return get_movie()

def change_state(user_answer, *args):
    set_button_state(user_answer)
    if not "user_answer" in st.session_state.quiz_data  == "":
        result = checkwinner(st.session_state.quiz_data["winner_movie"], st.session_state.quiz_data["user_answer"])
        st.success(result)
        del st.session_state.quiz_data  # Reset quiz data for next question
    elif "user_answer" in st.session_state.quiz_data == "":
        st.session_state.quiz_started = False        
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

def display_question(winner_movie_data):
    st.write("Which movie is this?")
    st.write(winner_movie_data.get("Plot"))
    col1, col2, col3 = st.columns([1, 1, 1]) 
    col1.button("Movie 1", on_click=change_state, args=('data1',), key=f"movie1")
    col2.button("Movie 2", key=f"movie2", on_click=change_state, args=('data2',))
    col3.button("Movie 3", key=f"movie3", on_click=change_state, args=('data3',))
    
    
    if st.button("Hint:", key=f"hint_button"):
        st.write(f"The Metacritic score is: {winner_movie_data.get('Metascore')}")

def calculate_image_heights(data1, data2, data3):
            return [
                get_image_dimensions(data1.get("Poster"))[1] if data1.get("Poster") else 0,
                get_image_dimensions(data2.get("Poster"))[1] if data2.get("Poster") else 0,
                get_image_dimensions(data3.get("Poster"))[1] if data3.get("Poster") else 0
            ]   

def display_quiz():
    if not "quiz_started" in st.session_state:
        st.session_state.quiz_started = False 
    
    if st.button("Start Quiz") and st.session_state.quiz_started == False:
        st.session_state.quiz_started = True

    elif st.session_state.quiz_started:   
        load_quiz_data()

        data1 = json.loads(st.session_state.quiz_data["data1"])
        data2 = json.loads(st.session_state.quiz_data["data2"])
        data3 = json.loads(st.session_state.quiz_data["data3"])
        winner_movie = st.session_state.quiz_data["winner_movie"]

        
        image_heights = calculate_image_heights(data1, data2, data3) 
        max_image_height = max(image_heights)

        # Calculate the longest title
        titles = [data1.get("Title"), data2.get("Title"), data3.get("Title")]
        max_title_length = max(len(title) for title in titles)
        
        # Calculate dynamic height
        title_height = max(60, max_title_length * 1.5) 

        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            display_movie_card(data1, title_height, max_image_height)
        with col2:
            display_movie_card(data2, title_height, max_image_height)
        with col3:
            display_movie_card(data3, title_height, max_image_height)
        
        st.divider()
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
        display_question(winner_movie_data=data)
        st.divider()
        st.button("End Quiz", on_click=change_state, args=(st.session_state.quiz_data["user_answer"],))
            

        
def load_quiz_data():
    if "quiz_data" not in st.session_state or st.session_state.quiz_data is None:
        st.session_state.quiz_data = {
            "data1": get_data(),
            "data2": get_data(),
            "data3": get_data(),
            "winner_movie": f"data{random.randint(1, 3)}",
            "user_answer": "",
        }
    
        
    

    
        
st.session_state
display_quiz()

