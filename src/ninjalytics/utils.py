def add_pitch_id(frame: pl.DataFrame) -> pl.DataFrame:
    """Adds a pitch_id column"""
    frame = frame.with_columns(
        pl.concat_str(
            [
                pl.col("game_pk"),
                pl.col("home_team"),
                pl.col("pitcher"),
                pl.col("at_bat_number"),
                pl.col("pitch_number"),
            ],
            separator="-",
        ).alias("pitch_id")
    )

    return frame


def get_season_start_end(season: int = 2024) -> list:
    """Returns a list with the first and last day of the regular season. Includes Tokyo + Korea series.""" 

    if season < 2021:
        print("Season must be >= 2021")
        return
    
    if season == 2021:
        return ["2021-04-01", "2021-10-03"]

    if season == 2022:
        return ["2022-04-07", "2022-10-05"]

    if season == 2023:
            return ["2023-03-30", "2023-10-01"]

    if season == 2024:
            return ["2024-03-20", "2024-10-03"]
    
    if season == 2025:
            return ["2025-03-18", "2025-09-28"]
    

