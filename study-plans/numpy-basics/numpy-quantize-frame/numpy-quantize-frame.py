import numpy as np

def quantize_and_frame(data, decimals, pad_width):
    """Returns: np.ndarray of shape (3, m+2p, n+2p), stacked rounded, floored, ceiled with zero-padding"""
    arr = np.array(data, dtype = np.float64)
    arr1 = np.round(arr, decimals = decimals)
    arr1 = np.pad(arr1, pad_width, mode = "constant", constant_values = 0)
    arr2 = np.floor(arr)
    arr2 = np.pad(arr2, pad_width, mode = "constant", constant_values = 0)
    arr3 = np.ceil(arr)
    arr3 = np.pad(arr3, pad_width, mode = "constant", constant_values = 0)
    return np.stack([arr1, arr2, arr3])
   
    