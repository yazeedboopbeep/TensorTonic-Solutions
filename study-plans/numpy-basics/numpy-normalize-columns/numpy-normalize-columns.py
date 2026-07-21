import numpy as np

def normalize(data):
    """Returns: np.ndarray of shape (m, n), z-score normalized per column"""
    array = np.array(data)
    mean = array.mean(axis=0)
    std = array.std(axis=0)
    return (array-mean)/std
    