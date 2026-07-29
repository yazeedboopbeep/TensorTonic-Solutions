import torch
import math

def compute_loss(pred, target, method, delta=1.0):
    """
    Returns: float, the mean loss value
    """
    target = torch.tensor(target)
    pred = torch.tensor(pred)
    match method:
        case "mse":
            loss = (1/target.shape[0]) * ((target-pred)**2).sum()
        case "cross_entropy":
            loss = (torch.logsumexp(pred, dim=1) - pred[torch.arange(pred.shape[0]), target]).mean()
        case "huber":
            a = pred - target
            loss = ((a.abs()<=delta).float() * 0.5 * a**2 + (1- (a.abs()<=delta).float()) * delta * (a.abs() - 0.5 * delta)).mean()
            
    return loss.item()