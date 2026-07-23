import numpy as np

def tile_diff(data, reps):
    """Returns: np.ndarray of shape (2, m*reps, n), stacked tiled array and padded differences"""
    arr = np.tile(np.array(data, dtype = np.float64), (reps, 1))
    arrDiff = np.diff(arr, axis = 0)
    arrDiff = np.pad(arrDiff, ((0, arr.shape[0] - arrDiff.shape[0]), (0, arr.shape[1] - arrDiff.shape[1])))
    return np.stack([arr, arrDiff])