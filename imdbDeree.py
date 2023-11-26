import pandas as pd

def load_subset_data(file_paths, num_rows=20000):
    data_frames = {}
    for file_path in file_paths:
        # Load a subset of data from each TSV file
        data = pd.read_csv(file_path, nrows=num_rows, sep='\t')
        data_frames[file_path] = data
    
    return data_frames

def explore_data(data_frames_dict):
    for file_name, df in data_frames_dict.items():
        print("File: ", file_name)
        print(df.info())


        

        df.replace(r'\\N', '//N', regex=True, inplace=True)

        numeric_columns = df.select_dtypes(include='number').columns
        for column in numeric_columns:
            df[column].fillna(df[column].mean(), inplace=True)
        
        ###### edo kai kato einai kati lathos
        print("Values missing: ")
        print(df.isnull().sum())

        print("----------------------------------------------------------------------------------")
                # Check for empty values in the DataFrame
      

        # Check for empty strings or whitespace-only strings
        contains_empty = (df.map(lambda x: isinstance(x, str) and x.strip() == '')).any().any()

        if contains_empty:
            print("The DataFrame contains empty or whitespace-only string values.")
        else:
            print("The DataFrame does not contain empty or whitespace-only string values.")

            ####### mexri edo



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


explore_data(data_frames_dict)

