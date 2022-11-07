"""This module handles data processing for ff_data_py.
"""

import pandas as pd
import nfl_data_py as nfl

def get_raw_pbp_data(min_year: int,
                     max_year: int | None = None,
) -> pd.DataFrame:
    """Retrieves raw play-by-play data as a pandas DataFrame.

    Args:
        min_year (int): Minimum year to retrieve data for. Will only retrieve
            data for this year if no max_year provided.
        max_year (int, optional): Maximum year to retrieve data for. If none
            provided, will only return data for min_year. Defaults to None.

    Returns:
        pd.DataFrame: NFL play-by-play data for the year range requested.
    """
    cols = [
        'desc',
        'play_id',
        'game_id',
        'game_date',
        'week',
        'qtr',
        'time',
        'down',
        'game_date',
        'posteam',
        'defteam',
    ]

    if max_year is None:
        years = [min_year]
    elif max_year is not None:
        years = list(range(min_year, max_year + 1))

    return nfl.import_pbp_data(years=years, columns=cols)
