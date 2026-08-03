import numpy as np


def euclidean_distance(x, y):
    """
    Returns: float, the Euclidean distance between x and y.
    """
    x, y = np.array(x), np.array(y)
    return np.sqrt(np.sum((x-y)**2))