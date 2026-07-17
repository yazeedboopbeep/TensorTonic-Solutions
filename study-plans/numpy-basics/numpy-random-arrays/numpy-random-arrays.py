import numpy as np

def generate_random_array(shape, kind, seed):
    """
    Returns: 2D ndarray of float64 random values
    """
    rng = np.random.RandomState(seed)
    match kind:
        case "normal":
            return rng.standard_normal(shape)
        case "uniform":
            return rng.random_sample(shape)