import numpy as np

def original_and_clipped(data, row_idx, lo, hi):
    """
    Returns: 2D ndarray of float64 with shape (2, ncols)
    """
    array = np.array(data, dtype = np.float64)
    row = array[row_idx].copy()
    return np.stack([row, np.clip(row, lo, hi)])