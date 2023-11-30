import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_ID = "arthurxboxelite"
CLIENT_ID = os.environ.get('CLIENT_ID')
SECRET_ID = os.environ.get('SECRET_ID')
SPOTIPY_REDIRECT_URI = os.environ.get('SPOTIPY_REDIRECT_URI')
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=SECRET_ID,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="playlist-modify-public"))
user_date = input("Digite a data para qual você quer viajar. O formato da data deve ser YYYY-MM-DD: ")


def get_song_titles(date: str) -> tuple[list[str], list[str]]:
    """Returns a list with the top 100 songs from the given date.

    :param date: Date in YYYY-MM-DD format.

    :return song_list: list with the songs names.
    """
    response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
    response.encoding = "utf-8"
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    # noinspection PyArgumentList
    songs = soup.select(selector="li h3", class_="c-title")
    # noinspection PyArgumentList
    artists = soup.select(selector="li ul li span", class_="c-label")
    print("\nObtendo as músicas para essa data...\n")

    unfiltered_song_list = [song.text.strip() for song in songs]
    unfiltered_artist_list = [artist.text.strip() for artist in artists]
    song_list = unfiltered_song_list[:100]
    artist_list = unfiltered_artist_list[::7]
    return (song_list, artist_list)


def get_songs_uris() -> list[str]:
    """Returns the song list with the songs names replaced with the songs URIs

    :return uris: List with the song URIs"""
    songs = get_song_titles(user_date)[0]
    artists = get_song_titles(user_date)[1]
    uris = []
    for song, artist in zip(songs, artists):
        result = sp.search(f"track: {song} artist: {artist} year: {user_date.split('-')[0]}")
        try:
            uris.append(result['tracks']['items'][0]['uri'])
        except IndexError:
            uris.append("MUSIC NOT FOUND")
    print("\nVerificando se existem no spotify...\n")
    return uris


def create_songs_playlist(uri_list):
    """Creates the playlist on spotify given the list with the songs URIs

    :param uri_list: List with the songs URIs"""
    playlist_name = f"{user_date} Billboard 100"
    sp.user_playlist_create(
        user=SPOTIFY_ID,
        name=playlist_name,
        description=f"Playlist criada automaticamente com as 100 melhores músicas na data {user_date.split('-')[2]}-"
                    f"{user_date.split('-')[1]}-{user_date.split('-')[0]}"
    )

    playlist_created_id = sp.user_playlists(SPOTIFY_ID)['items'][0]['id']
    sp.playlist_add_items(playlist_created_id, uri_list)
    print("\nCriando playlist...\n")


create_songs_playlist(get_songs_uris())
playlist_link = sp.user_playlists(SPOTIFY_ID)['items'][0]['external_urls']['spotify']

print(f"Playlist criada! Link: {playlist_link}")
