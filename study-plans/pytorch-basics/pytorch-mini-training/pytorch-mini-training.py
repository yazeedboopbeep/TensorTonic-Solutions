import torch
import torch.nn as nn

def train_epoch(model, dataloader, criterion, optimizer):
    """
    Returns: average loss over all batches (float)
    """
    #model.train()   # first line, before the loop
    average_loss = []
    for batch_idx, (batch, labels) in enumerate(dataloader):
        optimizer.zero_grad()
        y_hat = model(batch)
        loss = criterion(y_hat, labels)
        loss.backward()
        optimizer.step()
        average_loss.append(loss.item())
    return sum(average_loss)/len(average_loss)
            
            