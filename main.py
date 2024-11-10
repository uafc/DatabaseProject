import os
import sqlite3
import requests
from dotenv import load_dotenv

#loads api key from .env
load_dotenv() 
OMDB_API_KEY = os.getenv('OMDB_API_KEY')

#create database according to our database schema
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        imdb_id TEXT UNIQUE,
        title TEXT NOT NULL,
        poster_url TEXT
    )
''')
conn.commit()
conn.close()

#get movie info from omdb api
def fetch_movies_data(query):
    params = {
        'apikey': OMDB_API_KEY,
        's': query,
        'type': 'movie'
    }

    response = requests.get("http://www.omdbapi.com/", params=params)
    data = response.json()

    if data.get('Response') == 'True':
        return data.get('Search', [])
    else:
        print(f"No results found for '{query}'.")
        return []
    
def add_movie_to_db(imdb_id, title, poster_url): #todo
    pass

def delete_movie_from_db(imdb_id): #todo
    pass

#main
def main():
    search = input("Enter a movie name: ")
    movies = fetch_movies_data(search)

    if movies:
        print("Movies Found:")
        for movie in movies:
            print(f"Title: {movie['Title']}")
            print(f"IMDb ID: {movie['imdbID']}")
            print(f"Poster URL: {movie['Poster']}")
            print("-" * 20)

main()
