def create_release_agg_frame(frame: pl.DataFrame) -> pl.DataFrame:
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


def calc_centroid_distance(
    frame: pl.DataFrame, x_col: str, y_col: str, z_col: str, group_cols: list
) -> pl.DataFrame:
    """Given a 3D coordinate system, calculate the mean and sd distance to centroid

    Args:
        frame (pl.DataFrame): Dataframe with x, y, z, and group
        x_col (str): Column with x-coord. Ex: 'release_pos_x'
        y_col (str): Column with x-coord. Ex: 'release_pos_y'
        z_col (str): Column with x-coord. Ex: 'release_pos_z'
        group_cols (list): List of columns to group by. Ex: ['pitcher', 'pitch_type']

    Returns:
        pl.DataFrame: Aggregated data
    """

    get_centroid_x = pl.col(x_col).mean().alias("centroid_x")
    get_centroid_y = pl.col(y_col).mean().alias("centroid_y")
    get_centroid_z = pl.col(z_col).mean().alias("centroid_z")

    calc_euclidean_distance = (
        (
            (pl.col(x_col) - pl.col("centroid_x")) ** 2
            + (pl.col(y_col) - pl.col("centroid_y")) ** 2
            + (pl.col(z_col) - pl.col("centroid_z")) ** 2
        )
        .sqrt()
        .alias("distance")
    )

    agg_frame = (
        frame.group_by(group_cols)
        .agg(get_centroid_x, get_centroid_y, get_centroid_z)
        .join(frame, on=group_cols)
        .with_columns([calc_euclidean_distance])
        .group_by(group_cols)
        .agg(
            [
                pl.col("distance").mean().alias("mean_distance"),
                pl.col("distance").std().alias("std_dev_distance"),
            ]
        )
    )

    return agg_frame
