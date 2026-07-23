import numpy as np

def compare_correlations(a, b):
    """Returns: np.ndarray of shape (3, n, n), stacked correlation matrices"""
    a, b = np.array(a, dtype = np.float64), np.array(b, dtype = np.float64)
    return [np.corrcoef(a, rowvar = False), np.corrcoef(b, rowvar = False), np.corrcoef(np.vstack([a,b]), rowvar = False)]