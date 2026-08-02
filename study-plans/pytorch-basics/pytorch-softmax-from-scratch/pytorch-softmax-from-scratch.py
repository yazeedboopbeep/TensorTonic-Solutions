import torch

def softmax(logits):
    """
    Returns: tensor of same shape with softmax probabilities (each row sums to 1)
    """
    Z = torch.tensor(logits, dtype = torch.float32)
    MAX = torch.amax(Z, dim = 1, keepdim = True)
    Z_m = Z - MAX
    softmax = (torch.e**Z_m) / (torch.sum(torch.e**Z_m, dim = 1, keepdim =True))
    return softmax
