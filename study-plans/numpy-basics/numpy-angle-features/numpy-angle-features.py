import numpy as np

def angle_features(angles):
    """Returns: np.ndarray of shape (3, n), rows are sin, cos, tan"""
    array = np.array(angles)
    return np.stack([np.sin(array), np.cos(array), np.tan(array)], axis = 0)