import pandas as pd
import os

def load_csv(file_path):
    """
    Load a CSV file into a pandas DataFrame.
    
    Parameters:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Loaded data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    return pd.read_csv(file_path)

def clean_data(df):
    """
    Clean the dataset by removing duplicates and missing values.
    
    Parameters:
        df (pd.DataFrame): DataFrame to clean.
    
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    return df

def save_csv(df, file_path):
    """
    Save a pandas DataFrame to a CSV file.
    
    Parameters:
        df (pd.DataFrame): DataFrame to save.
        file_path (str): Path to save the CSV file.
    """
    df.to_csv(file_path, index=False)
