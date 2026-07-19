import numpy as np

def row_summary(data, threshold):
    """Returns: np.ndarray of shape (3, m, n), stacked element mask, any-filtered, all-filtered"""
    array = np.array(data)
    arr1 = (array > threshold).astype(np.float64)
    arr2 = np.where(np.expand_dims(np.any(array>threshold, axis = 1), axis = 1), array,  0)
    arr3 = np.where(np.expand_dims(np.all(array>threshold, axis = 1), axis = 1), array, 0)
    return np.stack([arr1, arr2, arr3], axis = 0)