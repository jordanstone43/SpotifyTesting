import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util


def artistRequest():
    artistURI = input("Enter the spotify URI of an Artist: ")
    return artistURI


def lookupArtist(artistURI):
    creds = SpotifyClientCredentials(
        client_id='984c118cabf84a479b24f822604ae886', client_secret='985146bd99f34d99a3312fe36dc483b7')
    sp = spotipy.Spotify(client_credentials_manager=creds)
    results = sp.artist(artistURI)
    print("Name: " + results['name'])
    print("Popularity: " + str(results['popularity']))
    print("Genres: " + ", ".join(results['genres']))
    print('\n')
