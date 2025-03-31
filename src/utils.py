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
