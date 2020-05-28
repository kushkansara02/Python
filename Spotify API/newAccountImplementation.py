# This script takes the dictionaries created by the previous script and parses through the data
# in order to add the exact shows and playlists to another account on Spotify

from spotipy_client import SpotipyClient
from itertools import islice

def splitDictionary(data, size = 100):
    # splits dictionary into dictionaries of size 100 by default, can be changed
    # this algorithm was originally created by thefourtheye and taken from stack overflow
    # https://stackoverflow.com/questions/22878743/how-to-split-dictionary-into-multiple-dictionaries-fast
    it = iter(data)
    for i in range(0, len(data), size):
        yield {k:data[k] for k in islice(it, size)}

# information unique to each user - needed for authentication
username = "your username"
client_id = "your client id"
client_secret = "your client secret"
redirect_uri = "https://google.ca/" #example redirect uri

# extracting dictionaries from text file
playlists_to_be_copied = eval(open("playlists_add.txt", "r").read())
playlists_to_be_followed = eval(open("playlists_follow.txt", "r").read())
shows = eval(open("shows.txt", "r").read())
tracks = eval(open("tracks.txt", "r").read())

### FOLLOW/COPY ALL NEEDED PLAYLISTS/PODCASTS ON NEW ACCOUNT ###

user = SpotipyClient(username, client_id, client_secret, redirect_uri) # creating user object

# extracting show IDs
shows_to_be_added = []
for show_id in shows.values():
    shows_to_be_added.append(show_id)

# following shows on new account
user.addShows(shows_to_be_added)

# playlist copying/following
for playlist in playlists_to_be_copied:
    tracks_all = tracks[playlist[0]]
    
    # only 100 tracks can be added at once, so the tracks dictionary needs to be split up
    tracks_playlist = splitDictionary(tracks_all)
    
    #creating a new playlist
    user.createCopyPlaylist(username, playlist[0], description = playlist[0])
    copy_playlist_id = user.getPlaylistID(playlist[0])
    
    for items in tracks_playlist:
        # adding all tracks in split up dictionaries into playlist
        user.addTracks(copy_playlist_id, items)

# following allocated playlists
for playlist in playlists_to_be_followed:
    user.followExistingPlaylist(playlist[1])

print("Process Completed")

### END REGION ###