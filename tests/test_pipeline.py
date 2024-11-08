import sys
from pathlib import Path
import os

# Add the src directory to the Python path
src_path = Path(__file__).parent.parent / "src"
sys.path.append(str(src_path))

# Now import from src
from src.data_loader import load_csv, save_csv
from src.api_fetcher import fetch_game_boxscore
from src.data_updater import update_game_data
from src.dag_pipeline import pipeline


import pandas as pd
import requests

def run_real_test():
    print("\n=== NHL Pipeline Real Test ===")
    
    # Test configuration
    test_file = "real_test_output.csv"
    game_id = "2023020001"
    
    try:
        # Create initial empty DataFrame
        initial_df = pd.DataFrame(columns=['gameID', 'team', 'score', 'date', 'venue', 'home_team', 'away_team'])
        initial_df.to_csv(test_file, index=False)
        
        print("\nFetching game data from NHL API...")
        # Fetch and process game data
        game_data = fetch_game_boxscore(game_id)
        
        if game_data:
            home_team = game_data['homeTeam']
            away_team = game_data['awayTeam']
            
            print(f"\nGame Details:")
            print(f"Date: {game_data['gameDate']}")
            print(f"Venue: {game_data['venue']['default']}")
            print(f"Home Team: {home_team['name']['default']} (Score: {home_team['score']})")
            print(f"Away Team: {away_team['name']['default']} (Score: {away_team['score']})")
            print(f"Status: {game_data['gameState']}")
            
            # Process home team data
            home_data = {
                'gameID': int(game_id),
                'team': home_team['placeName']['default'],
                'score': home_team['score'],
                'date': game_data['gameDate'],
                'venue': game_data['venue']['default'],
                'home_team': home_team['name']['default'],
                'away_team': away_team['name']['default']
            }
            
            # Process away team data 
            away_data = {
                'gameID': int(game_id),
                'team': away_team['placeName']['default'],
                'score': away_team['score'],
                'date': game_data['gameDate'],
                'venue': game_data['venue']['default'],
                'home_team': home_team['name']['default'],
                'away_team': away_team['name']['default']
            }
            
            # Update DataFrame with both teams
            df = pd.read_csv(test_file)
            df = update_game_data(df, home_data)
            df = update_game_data(df, away_data)
            
            # Save final results
            df.to_csv(test_file, index=False)
            
            print("\nFinal Data:")
            print(df)
            
            print("\n=== Game Statistics ===")
            print("\nHome Team Stats:")
            print(f"Shots on Goal: {home_team['sog']}")
            
            # Print player statistics for home team
            print("\nKey Players (Home):")
            for player in game_data['playerByGameStats']['homeTeam']['forwards']:
                if player['goals'] > 0 or player['assists'] > 0:
                    print(f"{player['name']['default']}: {player['goals']} goals, {player['assists']} assists")
            
            print("\nAway Team Stats:")
            print(f"Shots on Goal: {away_team['sog']}")
            
            # Print player statistics for away team
            print("\nKey Players (Away):")
            for player in game_data['playerByGameStats']['awayTeam']['forwards']:
                if player['goals'] > 0 or player['assists'] > 0:
                    print(f"{player['name']['default']}: {player['goals']} goals, {player['assists']} assists")
            
            print("\n✅ Test completed successfully!")
            print(f"- Game ID: {game_id}")
            print(f"- Match: {home_team['name']['default']} vs {away_team['name']['default']}")
            print(f"- Final score: {home_team['score']}-{away_team['score']}")
            
        else:
            print("\n⚠️ No data received from API")
            
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        print(traceback.format_exc())
    finally:
        if os.path.exists(test_file):
            os.remove(test_file)
            print("\nTest file cleaned up")

if __name__ == "__main__":
    print(f"Python path: {sys.path}")
    print(f"Current directory: {os.getcwd()}")
    run_real_test()
