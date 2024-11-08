import pandas as pd

def update_game_data(existing_df, new_data):
    """
    Update the game-level data with new data.
    
    Parameters:
        existing_df (pd.DataFrame): Existing game data.
        new_data (dict): New data to append.
    
    Returns:
        pd.DataFrame: Updated DataFrame.
    """
    new_df = pd.DataFrame([new_data])
    updated_df = pd.concat([existing_df, new_df], ignore_index=True)
    updated_df.drop_duplicates(inplace=True)
    return updated_df
