def create_pitcher_release_agg_frame(frame: pl.DataFrame) -> pl.DataFrame:
    """Creates aggregated summary statistics for pitcher release variables"""
    frame = frame.group_by(["pitcher", "pitch_type"]).agg(
        [
            pl.col("release_pos_x").mean().alias("release_pos_x_mean"),
            pl.col("release_pos_x").std().alias("release_pos_x_std"),
            pl.col("release_pos_y").mean().alias("release_pos_y_mean"),
            pl.col("release_pos_y").std().alias("release_pos_y_std"),
            pl.col("release_pos_z").mean().alias("release_pos_z_mean"),
            pl.col("release_pos_z").std().alias("release_pos_z_std"),
            pl.col("release_extension").mean().alias("release_extension_mean"),
            pl.col("release_extension").std().alias("release_extension_std"),
            pl.col("arm_angle").mean().alias("arm_angle_mean"),
            pl.col("arm_angle").std().alias("arm_angle_std"),
            pl.len().alias("count"),
        ]
    )

    return frame