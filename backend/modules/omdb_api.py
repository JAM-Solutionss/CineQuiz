from urllib import response
import requests
import json
import os
from dotenv import load_dotenv
from backend.modules.filter import filter

load_dotenv()
import streamlit as st

os.environ["OMDB_API"] = st.secrets['OMDB_API']

def get_API_response(search_parameter, request_type) -> dict:
    """
    Sends a request to the OMDB API and returns the response.

    Args:
        search_parameter (str): The search term or ID to query the API with.
        request_type (str): The type of request to make. Can be 'search', 'title', or 'imdbID'.

    Returns:
        dict: The JSON response from the API if successful, None otherwise.

    Raises:
        None, but prints error messages to console if API key is missing or request fails.

    Note:
        Requires the OMDB_API environment variable to be set with a valid API key.
    """    
    api_key = os.environ.get('OMDB_API')
    
    if api_key is None:
        print("Error: OMDB_API environment variable is not set.")
        return None

    match request_type:
        case 'search':
            url = f'http://www.omdbapi.com/?s={search_parameter}&apikey={api_key}'
        case 'title':
            url = f'http://www.omdbapi.com/?t={search_parameter}&apikey={api_key}'
        case 'imdbID':
            url = f'http://www.omdbapi.com/?i={search_parameter}&apikey={api_key}'
            
    print(f"Request URL: {url}")
    
    response = requests.get(url)        
    
    if response.status_code == 200:
        return response
    else:
        print(f"Error with the request: {response.status_code}")
        print(response.text)
        return None     

def filter_movie_data(data: dict) -> dict:
    filtered_data = {key: data[key] for key in filter if key in data}
    return filtered_data       

if __name__ == '__main__':
 pass