import pandas as pd

def drop_duplicates(data):
    """
    Returns: list [rows_before, rows_after, cleaned_data]
    """
    df = pd.DataFrame(data)

    return [df.shape[0], df.drop_duplicates().shape[0], df.drop_duplicates().to_dict("list")]