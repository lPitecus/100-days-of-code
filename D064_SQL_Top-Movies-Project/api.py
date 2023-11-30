import requests

TMDB_API_KEY = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhNThkZWUwNDk2OTk4ODc0YjYzMTFlMzY5NjdkZWM1NyIsInN1YiI6IjY1NWJiZjgwZjY3ODdhMDExZDVlOWQ4MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.udy3jtLMjf31oXLwhBi-1TLWhoiPINNe3E1PnEEgQQo"
headers = {
    "accept": "application/json",
    "Authorization": TMDB_API_KEY
}


def search_movie_by_name(movie_name: str) -> list:
    params = {
        "query": movie_name,
        "include_adult": "false",
        "language": "en-US",
        "page": 1
    }
    response = requests.get("https://api.themoviedb.org/3/search/movie", headers=headers, params=params).json()['results']
    return response


def search_movie_by_id(movie_id: str):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}", headers=headers).json()
    movie_info = {
        "title": response['title'],
        "img_url": f"https://image.tmdb.org/t/p/w500{response['poster_path']}",
        "year": int(response['release_date'][:4]),
        "description": response['overview']
    }
    return movie_info


print(search_movie_by_id("19995"))
