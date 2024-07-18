from urllib import response
import requests
import json
import os
from dotenv import load_dotenv
from filter import filter

load_dotenv()
import streamlit as st

os.environ["OMDB_API"] = st.secrets['OMDB_API']

def get_API_response_by_title(title) -> dict:
    api_key = os.environ.get('OMDB_API')
    
    if api_key is None:
        print("Error: OMDB_API environment variable is not set.")
        return
    
    url = f'http://www.omdbapi.com/?t={title}&apikey={api_key}'

    print(f"Request URL: {url}")
    
    response = requests.get(url)        
    
    if response.status_code == 200:
        return response
    else:
        print(f"Error with the request: {response.status_code}")
        print(response.text)
        return None
    
def get_API_response_by_search(keyword) -> dict:
    api_key = os.environ.get('OMDB_API')
    
    if api_key is None:
        print("Error: OMDB_API environment variable is not set.")
        return
    
    url = f'http://www.omdbapi.com/?s={keyword}&apikey={api_key}'

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