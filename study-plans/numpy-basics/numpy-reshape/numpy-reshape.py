import numpy as np

def reshape_array(data, operation):
    """
    Returns: ndarray of float64 with shape determined by the operation
    """
    arr = np.array(data, dtype = np.float64)
    match operation:
        case "flatten":
            return arr.flatten()
        case "transpose":
            return arr.T
        case "add_batch":
            list = [1]
            list += [dim for dim in arr.shape]
            return arr.reshape(list)
