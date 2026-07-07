import pandas as pd

def create_pivot(data, index, columns, values, aggfunc):
    """
    Returns: nested dict {column_value: {index_value: agg_result}}
    """
    return pd.pivot_table(pd.DataFrame(data), index = index, columns = columns, values = values, aggfunc = aggfunc, fill_value = 0).to_dict()