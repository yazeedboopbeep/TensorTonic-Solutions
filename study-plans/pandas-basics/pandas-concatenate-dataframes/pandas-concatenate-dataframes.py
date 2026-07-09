import pandas as pd

def concat_dataframes(dfs):
    """
    Returns: list [shape, data] where shape is [rows, cols]
    """
    data = pd.concat([pd.DataFrame(data) for data in dfs], ignore_index = True)
    return [list(data.shape), data.to_dict("list")]