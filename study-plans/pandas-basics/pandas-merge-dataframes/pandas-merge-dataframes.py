import pandas as pd

def merge_dataframes(left, right, on, how):
    """
    Returns: dict of column to value lists
    """
    leftDF = pd.DataFrame(left)
    rightDF = pd.DataFrame(right)
    return pd.merge(leftDF, rightDF, on=on, how=how).to_dict("list")