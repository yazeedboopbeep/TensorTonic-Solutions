import numpy as np

def norm_diff(a, b, lo, hi):
    """Returns: np.ndarray of absolute differences after clipping and rescaling to [0, 1]"""
    a = np.clip(np.array(a), lo, hi, dtype = np.float64)
    b = np.clip(np.array(b), lo, hi, dtype = np.float64)
    a = (a-lo)/(hi-lo)
    b = (b-lo)/(hi-lo)
    return np.abs(a-b)