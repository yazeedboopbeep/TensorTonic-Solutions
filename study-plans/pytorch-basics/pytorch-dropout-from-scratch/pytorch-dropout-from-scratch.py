import torch
import torch.nn as nn

class Dropout(nn.Module):
    def __init__(self, p=0.5):
        super().__init__()
        self.p = p

    def forward(self, x):
        """
        Returns: tensor with dropout applied
        """
        x = torch.tensor(x, dtype = torch.float32)
        
        if self.training is True:
            if self.p == 1:
                x = torch.zeros_like(x)
            else:
                x = (x * (torch.bernoulli(torch.full(x.shape, 1-self.p, dtype = torch.float32)))) / (1-self.p)
        return x
        
