# Import the random and os modules
import random
import os

# Define a function called get_line that returns a random line from the lyrics
def get_line():
    # Specify the file path of the albums folder
    albums_path = "C:\\Users\\maver\\Documents\\Python\\Projects\\tweepy-bots\\albums"

    # Get the list of album folders in the albums folder
    albums = [folder for folder in os.listdir(albums_path) if os.path.isdir(os.path.join(albums_path, folder))]

    # Choose a random album from the list
    random_album = random.choice(albums)

    # Get the list of song files in the random album folder
    songs = [file for file in os.listdir(os.path.join(albums_path, random_album)) if file.endswith(".txt")]

    # Choose a random song from the list
    random_song = random.choice(songs)

    # Open the random song file
    with open(os.path.join(albums_path, random_album, random_song), "r") as f:
        # Read the file and split it into a list of lines
        lines = f.read().split("\n")

    # Ignore the first line of the lyrics by slicing the list from the second element
    lines = lines[1:]

    # Filter out any line that has "\" or "Embed" using list comprehension
    lines = [line for line in lines if "\\" not in line and "Embed" not in line]

    # Choose a random line from the list
    random_line = random.choice(lines)

    # Return the random line
    return random_line
