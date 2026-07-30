import torch


def batch_norm(X, gamma, beta, eps=1e-5):
    """
    Returns: tensor of shape (N, D), the batch-normalized output
    """

    X = torch.tensor(X, dtype = torch.float32)
    mu = X.mean(axis = 0)
    sigma = X.std(axis = 0, correction = 0)
    X_hat = (X-mu)/(torch.sqrt(sigma**2 + eps))
    Y = gamma * X_hat + beta
    return Y
