import numpy as np

def norm_gate(X, W, threshold):
    """Returns: np.ndarray of shape (n, k), gated projection where rows below threshold are zeroed"""
    X = np.array(X, dtype = np.float64)
    W = np.array(W, dtype = np.float64)
    Y = X@W
    norm = np.linalg.norm(Y, axis = 1)
    G = (norm >= threshold).astype(np.float64)
    Z = Y * G[:, None]
    return Z
   