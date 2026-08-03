import numpy as np

def vector_norms(v):
    """
    Returns: float64 array of shape (3,) containing [L1, L2, L-inf] norms.
    """
    v = np.array(v, dtype = np.float64)
    L1 = np.sum(np.abs(v))
    L2 = np.sqrt(np.sum(v**2))
    Linf = np.max(np.abs(v))
    return [L1, L2, Linf]