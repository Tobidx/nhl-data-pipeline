import requests
import logging

BASE_URL = "https://api-web.nhle.com/v1/"

def fetch_game_boxscore(game_id):
    """
    Fetch the boxscore for a specific game ID using the NHL API.
    
    Parameters:
        game_id (str): Unique game ID.
    
    Returns:
        dict: Boxscore data in JSON format.
    """
    url = f"{BASE_URL}gamecenter/{game_id}/boxscore"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching game boxscore for {game_id}: {e}")
        return None
