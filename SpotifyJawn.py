import sys
import os
import spotipy
import webbrowser
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

client_credentials_manager = SpotifyClientCredentials(
    client_id='984c118cabf84a479b24f822604ae886', client_secret='985146bd99f34d99a3312fe36dc483b7')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
results = sp.artist('spotify:artist:0iEtIxbK0KxaSlF7G42ZOp')
imgUrl = results['images'][0]['url']
sp.trace = True  # turn on tracing
sp.trace_out = True  # turn on trace out
webbrowser.open_new_tab(imgUrl)

# DEez
