import pandas as pd

def clean_df(df):
    columns_to_drop = ['Album', 'Playlist name', 'Type', 'ISRC']
    return df.drop(columns_to_drop, axis=1)


def df_tracks(csv_file):
    df = pd.read_csv(csv_file)
    return clean_df(df)



