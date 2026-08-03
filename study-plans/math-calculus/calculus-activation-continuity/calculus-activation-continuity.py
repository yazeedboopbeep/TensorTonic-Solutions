import numpy as np

def activation_continuity_analysis(x):
    """
    Returns: dict mapping 'relu', 'leaky_relu', 'gelu' to lists of non-differentiable x values
    """
    x = np.array(x)
    pts = np.sum(x == 0)
    res = [0.0] * pts
    return {
        'relu': res,
        'leaky_relu': res,
        'gelu': []
    }