import torch

def reshape_tensor(x, op):
    """
    Returns: list
    """
    x = torch.Tensor(x)
    match op:
        case "flatten":
            return (x.flatten()).tolist()
        case "squeeze":
            return (x.squeeze()).tolist()
        case "transpose":
            return (x.T).tolist()
