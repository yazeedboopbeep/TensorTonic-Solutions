import pandas as pd

def change_dtype(data, column, target_type):
    """
    Returns: list [dtypes_before, dtypes_after] (both dicts)
    """
    df = pd.DataFrame(data)
    new_df = df.copy()
    new_df[column] = new_df[column].astype(target_type)
    return [df.dtypes.astype(str).to_dict(), new_df.dtypes.astype(str).to_dict()]

    