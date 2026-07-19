import numpy as np

def select_by_index(arr, indices, axis):
    """
    Returns: 2D ndarray of float64
    """
    array = np.array(arr, dtype = np.float64)
    match axis:
        case 0:
            return array[indices,:]
        case 1:
            return array[:, indices]