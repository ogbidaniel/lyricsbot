# Import the random and os modules
import random
import os

def get_line():
    # Specify the file path of the albums folder
    albums_path = "Ekwesu/billywoodsbot/albums"

    # Get the list of album folders in the albums folder
    albums = [folder for folder in os.listdir(albums_path) if os.path.isdir(os.path.join(albums_path, folder))]

    random_album = random.choice(albums)

    songs = [file for file in os.listdir(os.path.join(albums_path, random_album)) if file.endswith(".txt")]

    # Choose a random song from the list
    random_song = random.choice(songs)

    # Open the random song file
    with open(os.path.join(albums_path, random_album, random_song), "r") as f:
        # Read the file and split it into a list of lines
        lines = f.read().split("\n")

    # Ignore the first line of the lyrics
    lines = lines[1:]

    # Filters out any line that has "\" or "Embed"
    lines = [line for line in lines if "\\" not in line and "Embed" not in line]

    # Choose a random line from the list
    random_line = random.choice(lines)

    return random_line
