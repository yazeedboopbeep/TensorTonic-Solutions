import pandas as pd

def boolean_filter(data, column, threshold):
    """
    Returns: dict with 'filtered_data' (dict) and 'count' (int)
    """
    df = pd.DataFrame(data)
    filteredData = df[df[column] > threshold]
    return {'filtered_data': filteredData.to_dict("list"),
                'count': filteredData.shape[0]
               }