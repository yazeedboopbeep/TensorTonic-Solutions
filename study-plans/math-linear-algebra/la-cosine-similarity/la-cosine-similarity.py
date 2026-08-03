import numpy as np

def cosine_similarity(a, b):
    """
    Returns: float in [-1, 1], cosine similarity between a and b.
    """
    a, b = np.array(a), np.array(b)
    if (np.sum(a) == 0 or np.sum(b) == 0): return 0
    return (a @ b)/(np.linalg.norm(a) * np.linalg.norm(b))