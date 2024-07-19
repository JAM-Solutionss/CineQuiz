import streamlit as st
import json
from backend.modules.random_movie import get_movie_title
from backend.modules.random_movie import get_movie_data
from backend.modules.random_movie import get_random_keyword
from frontend.webpages.explanation import explanation
from frontend.webpages.movie_popup import movie_popup
import random
import requests
from PIL import Image
from io import BytesIO
from backend.modules.css import load_css


st.set_page_config(layout="wide")

# Load custom CSS
st.markdown(load_css(r'frontend/styles.css'), unsafe_allow_html=True)

st.markdown("""
<style>
    /* Your custom CSS here */
    .stNavigationMenu {
        background-color: #f1f1f1;
    }
</style>
""", unsafe_allow_html=True)

st.title("CineQuiz")


def game_status():
    card_number, card_score =  st.columns(2)
    if "round" in st.session_state == 10:
          st.success("Finished")
          st.write(f"Your score is {st.session_state['score'] / 10 * 100}%")
          end_game()
          st.rerun()
    elif "round" in st.session_state != 10:
          card_number.header(f"Round {st.session_state['round']}")
          card_score.header(f"Score: {st.session_state['score'] / 10 * 100}% in {st.session_state['round']} rounds")
     

def add_score_counter():
     st.session_state['score'] +=  1
     st.session_state['round'] +=  1

def subtract_score_counter():
     if not st.session_state['score'] == 0:
        st.session_state['score'] -=  1
     st.session_state['round'] +=  1

def set_button_state(user_answer):
     st.session_state.quiz_data['user_answer'] = user_answer
     
def end_game():
     del st.session_state.quiz_started
     del st.session_state.quiz_data
     del st.session_state.score
     del st.session_state.round
    
     

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
          movie_popup(data=st.session_state.temp_movie)
          add_score_counter()
          return "Correct Answer"
     else:
          movie_popup(data=st.session_state.temp_movie)
          subtract_score_counter()
          return "Incorrect Answer"

def get_data(title) -> dict:
    data = get_movie_data(title)
    #test = json.loads(data)
    #if test.get("Title") is None:
    #    return get_data(title)  # Retry if title is not found
    return data

def generate_keyword(keyword) -> str:
     return get_movie_title(keyword)

def change_state(user_answer, *args):
    set_button_state(user_answer)
    if not "user_answer" in st.session_state.quiz_data  == "":
        result = checkwinner(st.session_state.quiz_data["winner_movie"], st.session_state.quiz_data["user_answer"])
        if 'Incorrect' in result:
            st.error(result, icon="❌")
        else:
            st.success(result, icon="✅")
        del st.session_state.quiz_data  # Reset quiz data for next question
    elif "user_answer" in st.session_state.quiz_data is None:
        st.session_state.quiz_started = False        
        del st.session_state.quiz_data  


def display_movie_card(data, title_height, image_height):
                with st.container():
                    st.markdown(f"""
                        <div class="cards">
                            <h2 class="cardHeader">{data.get("Title")}</h2>
                            <img src="{data.get("Poster")}">
                            <p class="Year">{data.get("Year")} | {data.get("Genre")}</p>
                            <p class="Meta">Metacritic: {data.get("Metascore")}</p>
                        </div>
                        """, unsafe_allow_html=True)

def display_question(winner_movie_data):
    st.header("Which movie is this?")
    st.subheader(winner_movie_data.get("Plot"))
    col1, col2, col3 = st.columns([1, 1, 1])
      
    col1.button("Movie 1", on_click=change_state, args=('data1',), key=f"movie1")
    col2.button("Movie 2", key=f"movie2", on_click=change_state, args=('data2',))
    col3.button("Movie 3", key=f"movie3", on_click=change_state, args=('data3',))
    left, middle, right = st.columns([1, 1, 1])
    with middle:
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
    
        
    if not st.session_state.quiz_started: 
        if st.button("Start Quiz"):
            explanation()
            st.session_state.quiz_started = True
        
                
                
            
            
    
    if st.session_state.quiz_started:
        
        with st.spinner('Loading quiz data...'):
            load_quiz_data()
        data1 = json.loads(st.session_state.quiz_data["data1"])
        data2 = json.loads(st.session_state.quiz_data["data2"])
        data3 = json.loads(st.session_state.quiz_data["data3"])
        winner_movie = st.session_state.quiz_data["winner_movie"]

        game_status()
        st.divider()
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
        
        
        if winner_movie == "data1":
            data = data1
        elif winner_movie == "data2":
            data = data2
        elif winner_movie == "data3":
            data = data3
        else:
            data = None
        st.divider() 
        set_temp_movie(data)
        display_question(winner_movie_data=data)
        st.divider()
        st.button("End Quiz", on_click=end_game, key="end_quiz", type="primary")            



     
def set_temp_movie(data):
   st.session_state['temp_movie'] = data

def load_quiz_data():
    if "quiz_data" not in st.session_state or st.session_state.quiz_data is None:
        titles = []
        for i in range(3):
            title = get_random_keyword()
            while title in titles:
                title = get_random_keyword()
            titles.append(title)
        
        st.session_state.quiz_data = {
            "data1": get_data(titles[0]),
            "data2": get_data(titles[1]),
            "data3": get_data(titles[2]),
            "winner_movie": f"data{random.randint(1, 3)}",
            "user_answer": "",
        }
    if "score" not in st.session_state:
           st.session_state.score = 0   
    if "round" not in st.session_state:
            st.session_state.round = 1
    if "temp_movie" not in st.session_state:
        st.session_state.temp_movie = {}
   
    
        
  
display_quiz()

