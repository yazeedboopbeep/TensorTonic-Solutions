import numpy as np

def filter_and_extract(data, row_start, row_stop, threshold):
    """
    Returns: 1D ndarray of float64
    """
    arr = np.array(data)
    arraux = arr[row_start:row_stop]
    return arraux[arraux > threshold].astype(np.float64)