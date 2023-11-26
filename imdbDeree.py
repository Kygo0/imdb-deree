import pandas as pd

def load_subset_data(file_paths, num_rows=20000):
    data_frames = {}
    for file_path in file_paths:
        # Load a subset of data from each TSV file
        data = pd.read_csv(file_path, nrows=num_rows, sep='\t')
        data_frames[file_path] = data
    
    return data_frames

# List of file paths to your TSV files
file_paths = [
    'D:\imdb\data_name_basics.tsv',
    'D:\imdb\data_title_akas.tsv',
    'D:\imdb\data_title_basics.tsv',
    'D:\imdb\data_title_crew.tsv',
    'D:\imdb\data_title_episode.tsv',
    'D:\imdb\data_title_principles.tsv',
    'D:\imdb\data_title_rating.tsv'
]

# Example usage:
data_frames_dict = load_subset_data(file_paths, num_rows=20000)


