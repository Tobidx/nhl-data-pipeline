import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from data_loader import load_csv, save_csv
from api_fetcher import fetch_game_boxscore
from data_updater import update_game_data



def pipeline(game_ids, file_path):
    """
    Main pipeline for processing game data.
    
    Parameters:
        game_ids (list): List of game IDs to process.
        file_path (str): Path to the dataset CSV file.
    """
    existing_data = load_csv(file_path)
    
    for game_id in game_ids:
        new_data = fetch_game_boxscore(game_id)
        if new_data:
            existing_data = update_game_data(existing_data, new_data)
    
    save_csv(existing_data, file_path)
