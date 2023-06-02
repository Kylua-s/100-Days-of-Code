"""
This program allows users to travel back in time by using a specific date and retrieving the Billboard Hot 100 chart for
that date. It then searches for the corresponding songs on Spotify and creates a private playlist with those songs.
"""
import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime, date

OAUTH_AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
OAUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"
CLIENT_ID = "YOUR CLIENT ID"
CLIENT_SECRET = "YOUR CLIENT SECRET"
REDIRECT_URI = "YOUR REDIRECT URI"
SCOPE = "playlist-modify-private"


# Function to check if a date string is valid
def is_valid_date(date_string):
    try:
        # Attempt to parse the date string
        date_obj = datetime.strptime(date_string, "%Y-%m-%d").date()

        # Check if the date is before August 4, 1958
        if date_obj < date(1958, 8, 4):
            print("The earlierst possible date is the August 4, 1958")
            return False

        # Check if the date is today or earlier
        if date_obj > date.today():
            print("The date can't be in the future.")
            return False

        return True

    except ValueError:
        print("The provided date is invalid. Please enter the date in the format yyyy-mm-dd.")
        return False


print("Welcome to the Music Time Machine!")

# Prompt the user to enter a date
user_input = input("Enter the date you want to travel to (YYYY-MM-DD): ")

# Check if the entered date is valid
if is_valid_date(user_input):
    # Retrieve data from the Billboard Hot 100 chart for the given date
    response = requests.get("https://www.billboard.com/charts/hot-100/" + user_input)
    billboard_data = response.text

    # Parse the HTML data using BeautifulSoup
    soup = BeautifulSoup(billboard_data, "html.parser")

    # Extract song titles
    songs = soup.find_all(name="h3", id="title-of-a-story", class_="u-line-height-125")
    song_titles = [title.getText().strip("\n\t") for title in songs]

    # Extract artist names
    artists = soup.find_all(name="span", class_="u-max-width-330")
    artist_names = [name.getText().strip("\n\t") for name in artists]

    # Create a dictionary mapping song titles to artist names
    song_and_artist = dict(zip(song_titles, artist_names))

    print(song_and_artist)
    print("\nSearching for songs on Spotify and creating new playlist...")

    # Authenticate and authorize with Spotify using Spotipy
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=SCOPE,
            show_dialog=True,
            cache_path="token.txt"
        )
    )

    # Get the user's Spotify ID
    user_id = sp.current_user()["id"]

    song_uris = []
    for (song, artist) in song_and_artist.items():
        try:
            # Search for the song on Spotify
            result = sp.search(q=f"track:{song} artist:{artist}", type="track")
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"The song '{song}' by '{artist}' couldn't been found.")

    print(f"Number of songs found: {len(song_uris)}")

    # Create a new private playlist on Spotify
    playlist = sp.user_playlist_create(user=user_id, name=f"{user_input} Billboard 100", public=False)

    # Add the found songs to the playlist
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

    print(f"New playlist '{user_input} Billboard 100' successfully created on Spotify!")
