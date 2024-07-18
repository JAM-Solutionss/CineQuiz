import requests
import json
import os
from dotenv import load_dotenv
import random
from backend.modules.filter import filter, common_search_words
from backend.modules.omdb_api import get_API_response, filter_movie_data
import streamlit as st
load_dotenv()

os.environ["OMDB_API"] = st.secrets['OMDB_API']

def get_movie_title(keyword):
    """
    Retrieve a movie title containing the specified keyword.

    This function searches for movies using the OMDB API and returns the title
    of the first movie that contains the given keyword in its title.

    Args:
        keyword (str): The keyword to search for in movie titles.

    Returns:
        str: A JSON-formatted string containing the movie title if found,
             or None if no matching movie is found.

    Prints:
        - "No movies found with the specified word in the title." if no matching movies are found.
        - Error messages with status code and response text if the API request fails.
    """    
    response = get_API_response(keyword, 'search')

    if response is not None:
        data = response.json()
        if data['Response'] == 'True':
            for movie in data['Search']:
                if keyword.lower() in movie['Title'].lower():
                    result = json.dumps(movie['Title'], indent=4)
                    return result
        print("No movies found with the specified word in the title.")
    else:
        print(f"Error with the request: {response.status_code}")
        print(response.text)

def get_movie_data(keyword):
    """
    Retrieve detailed movie data for a given keyword.

    This function fetches movie data from the OMDB API using the provided keyword,
    filters the retrieved data, and returns it in a JSON format.

    Args:
        keyword (str): The keyword or movie title to search for.

    Returns:
        str: A JSON-formatted string containing the filtered movie data if successful,
             or None if an error occurs.

    Prints:
        - Error message if the API response is None.
    """
    response = get_API_response(keyword, 'title')

    if response is not None:
        data = response.json()
        filtered_data = filter_movie_data(data)
        return json.dumps(filtered_data, indent=4)
    else:
        print(f"Error getting movie data. Response is None.")
        return None

def get_random_keyword():
    random_keyword = random.choice(common_search_words)
    return random_keyword

if __name__ == '__main__':
    # title = 'The Shawshank Redemption'
    # title = 'ecwds'
    # resp = get_API_response(title)
    # d = get_movie_data(title)
    # print(d)
    # print(resp.json())
    # movie = get_movie_title('love')
    # print(movie)
    gmovie = get_movie_data('love')
    print(gmovie)