
def get_pitcher_data(pitcher_id: int, season: int = None, start: str = None, stop: str = None) -> pl.DataFrame:
    if season:
        print(f"Returning data from the {season} season for {pitcher_id}")

    else:
        print(f"Returning data from {start} to {stop} for {pitcher_id}")


def load_pitchers():
    """Load names and mlbids for all pitchers from 2021-2024"""

 def load_pitch_data(season: int) -> pl.DataFrame:
    """Load all statcast pitch data for a given season. It is recommended to save this off."""
    
       