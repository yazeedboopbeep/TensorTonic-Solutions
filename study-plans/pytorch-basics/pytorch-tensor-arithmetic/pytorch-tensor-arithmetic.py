import torch

def tensor_op(x, y, op):
    """
    Returns: list (result tensor converted via .tolist())
    """
    x, y = torch.tensor(x), torch.tensor(y)
    match op:
        case "add":
            return (x + y).tolist()
        case "multiply":
            return (x * y).tolist()
        case "matmul":
            return (x @ y).tolist()
        case "power":
            return (x**y).tolist()
        case "max":
            return torch.max(x, y).tolist()
            