import numpy as np

def summarize(data, axis):
    """Returns: np.ndarray of shape (4, k), rows are mean, std, min, max"""    
    arr = np.array(data)
    return np.stack([arr.mean(axis = axis), arr.std(axis = axis), arr.min(axis = axis), arr.max(axis = axis)], axis = 0)