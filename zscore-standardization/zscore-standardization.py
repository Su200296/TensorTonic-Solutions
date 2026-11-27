import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    # Write code here
    X= np.asarray(X,dtype = float)
    x_std = np.std(X,keepdims=True,axis = axis)
    x_mean = np.mean(X,keepdims=True,axis = axis)
    y = np.where(x_std > eps,x_std,1.0)
    X_norm = (X - x_mean) / y

    return X_norm