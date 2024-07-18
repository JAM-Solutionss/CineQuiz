import requests
import json
import os
from dotenv import load_dotenv
import random
from filter import filter, common_search_words
from omdb_api import get_API_response
import streamlit as st
load_dotenv()

os.environ["OMDB_API"] = st.secrets['OMDB_API']

def get_movie(keyword):
    
    response = get_API_response(keyword, 'search')

    if response is not None:
        data = response.json()
        print(data)
        if data['Response'] == 'True':
            for movie in data['Search']:
                if keyword.lower() in movie['Title'].lower():
                    result = json.dumps(movie['Title'], indent=4)
                    return result
        print("No movies found with the specified word in the title.")
    else:
        print(f"Error with the request: {response.status_code}")
        print(response.text)

def get_movie_data(title):

    response = get_API_response_by_title(title)

    if response is not None:
        data = response.json()
        filtered_data = filter_movie_data(data)
        return json.dumps(filtered_data, indent=4)
    else:
        print(f"Error getting movie data. Response is None.")
        return None

def get_random_word():
    random_word = random.choice(common_search_words)
    return random_word

if __name__ == '__main__':
    # title = 'The Shawshank Redemption'
    # title = 'ecwds'
    # resp = get_API_response(title)
    # d = get_movie_data(title)
    # print(d)
    # print(resp.json())
    movie = get_movie('love')
    print(movie)