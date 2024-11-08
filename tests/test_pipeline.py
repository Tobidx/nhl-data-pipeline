import pytest
import pandas as pd
import os
import sys
from src.dag_pipeline import pipeline

# Test data path
TEST_DATA_DIR = "tests/test_data"
TEST_FILE_PATH = os.path.join(TEST_DATA_DIR, "test_game_overview.csv")

@pytest.fixture(autouse=True)
def setup_test_environment():
    """Setup test environment"""
    os.makedirs(TEST_DATA_DIR, exist_ok=True)
    yield
    # Cleanup
    if os.path.exists(TEST_FILE_PATH):
        os.remove(TEST_FILE_PATH)

def test_pipeline_single_game():
    game_ids = ["2023020001"]
    pipeline(game_ids, TEST_FILE_PATH)
    
    assert os.path.exists(TEST_FILE_PATH)
    df = pd.read_csv(TEST_FILE_PATH)
    assert not df.empty
    assert "gameID" in df.columns

def test_pipeline_multiple_games():
    game_ids = ["2023020001", "2023020002"]
    pipeline(game_ids, TEST_FILE_PATH)
    
    df = pd.read_csv(TEST_FILE_PATH)
    assert len(df) >= len(game_ids)
