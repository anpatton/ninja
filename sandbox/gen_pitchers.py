seasons = [2021, 2022, 2023, 2024]
season_list = []

for season in seasons:
    print(season)
    season_frame = pl.from_pandas(pb.pitching_stats_bref(season))
    season_frame = (season_frame
                        .filter((pl.col("Lev") == "Maj-NL") | (pl.col("Lev") == "Maj-AL"))
                        .select(["mlbID", "G", "IP", "ERA", "WHIP", "SO9"])
                        .with_columns(pl.lit(season).alias("season"))
                        .with_columns(pl.col("mlbID").cast(pl.Int64)))
    season_list.append(season_frame)

frame = pl.concat(season_list)
frame = frame.rename({col: col.lower() for col in frame.columns})
players = frame["mlbid"].unique().to_list()
player_info = pb.playerid_reverse_lookup(player_ids=players)
player_info = player_info[["key_mlbam", "name_last", "name_first", "mlb_played_first", "mlb_played_last"]]
player_info = pl.from_pandas(player_info)
player_info = (player_info.with_columns((pl.col("name_first") + " " + pl.col("name_last")).alias("player_name"))
                            .with_columns(pl.col("player_name").str.to_titlecase().alias("player_name")))
player_info = player_info.rename({"key_mlbam": "mlbid"}).select(["mlbid", "player_name", "mlb_played_first", "mlb_played_last"])
frame = frame.join(player_info, on = "mlbid", how = "left")
frame = frame.select(["mlbid", "player_name", "season", "g", "ip", "era", "whip", "so9", "mlb_played_first", "mlb_played_last"])
frame.write_parquet("pitchers.parquet")