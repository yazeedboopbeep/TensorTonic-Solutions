import numpy as np

def sigmoid_squeeze_analysis(x):
    """
    Returns: dict with 'bounds' (list of [lower, sigmoid, upper] triples) and 'is_saturated' (list of bools)
    """
    x = np.array(x)

    def sigmoid(x):
        return (1+np.exp(-x))**(-1)
    lower = np.maximum(0, 1-np.exp(-x))
    upper = np.minimum(1, np.exp(x))
    is_saturated = (np.minimum(sigmoid(x), 1 - sigmoid(x)) < 1e-4)
    return {
        "bounds": (np.array([lower, sigmoid(x), upper])).T,
        "is_saturated": is_saturated
    }
    
