import numpy as np

def huber_loss(x, y, delta):
    for i in range(len(y)):
        huber_mae = delta * (np.abs(y[i]-x[i]) - 0.5 * delta)
        huber_mse = 0.5*(y[i] - x[i])**2
    if np.abs(y[i] - x[i]) <= delta:
        return huber_mse
    else:
        return huber_mae