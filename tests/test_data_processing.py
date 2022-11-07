"""Tests for the data_processing module.
"""

from ff_data_py import data_processing as dp

def test_get_raw_pbp_data():
    """Testing the output of the get_raw_pbp_data() function

    This test uses the 2015 dataset for the sake of example. As this data is
    historical, it should not change. Therefore, test is done using the length
    of the returned dataframe, which should remain consistent. Possible reasons
    for failure could be if the data somehow changes in the future, or if no
    connection to the server was established (in which case nfl_data_py merely
    returns an empty dataframe with length of 0).
    """
    df = dp.get_raw_pbp_data(2015)
    assert len(df) == 48869, "2015 dataset should have length of 48,869"
