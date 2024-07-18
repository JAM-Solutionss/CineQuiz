import requests
import json
import os
from dotenv import load_dotenv
from filter import *

load_dotenv()

def get_movie(title):
    api_key = os.environ.get('OMDB_API')
    
    if api_key is None:
        print("Error: OMDB_API environment variable is not set.")
        return
    
    url = f'http://www.omdbapi.com/?t={title}&apikey={api_key}'

    print(f"Request URL: {url}")

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        filtered_data = {key: data[key] for key in filter if key in data}
        return json.dumps(filtered_data, indent=4)
    else:
        print(f"Error with the request: {response.status_code}")
        print(response.text)

if __name__ == '__main__':
    title = 'The Shawshank Redemption'
    get_movie(title)