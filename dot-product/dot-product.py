import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    x_arr = np.asarray(x, dtype=np.float64)
    y_arr = np.asarray(y, dtype=np.float64)
    
    if x_arr.shape != y_arr.shape:
        raise ValueError("Input vectors must have the same shape.")
        
    return float(np.dot(x_arr, y_arr))