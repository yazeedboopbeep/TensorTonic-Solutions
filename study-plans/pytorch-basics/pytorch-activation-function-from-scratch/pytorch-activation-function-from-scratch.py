import torch

def activate(x, method="relu"):
    """
    Returns: list (activated tensor converted via .tolist())
    """
    x = torch.tensor(x, requires_grad=True, dtype = torch.float32)
    match method:
        case "relu":
            y = (x > 0).float() * x
        case "sigmoid":
            y = 1/(1+(torch.e)**(-x))
        case "tanh":
            y = (torch.e**(x) - torch.e**(-x))/(torch.e**(x) + torch.e**(-x))

        case "leaky_relu":
            y = torch.where(x>0, x, 0.01*x)


    return y.tolist()
            