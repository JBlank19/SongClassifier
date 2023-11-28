import pandas as pd
import json

# Load the datasets
artists = pd.read_csv('cleaned_artists.csv')
split_file = pd.read_parquet('tracks_features.parquet')

# Convert the genres in artists.csv from string representation of list to actual list
# and create a dictionary for quick genre lookup based on artist ID
genre_lookup = pd.Series(artists['genres'].apply(eval).values, index=artists['id']).to_dict()

# Define a function to find genres for a list of artist IDs
def find_genres(artist_ids):
    return [genre for artist_id in artist_ids if artist_id in genre_lookup for genre in genre_lookup[artist_id]]

# Process each row in split_file
split_file['artist_ids'] = split_file['artist_ids'].apply(eval)  # Convert artist_ids string to list
split_file['genres'] = split_file['artist_ids'].apply(find_genres)

# Filter out rows without genres
split_file = split_file[split_file['genres'].map(bool)]

# Convert genres list to JSON string
split_file['genres'] = split_file['genres'].apply(json.dumps)

# Save the modified DataFrame
split_file.to_parquet('clean_genre_data.parquet', index=False)
