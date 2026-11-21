import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    x = np.asarray(x,dtype = float)
    pmf = np.where(x == 1, p, np.where(x == 0, 1.0 - p, 0.0))
    
    mean = float(p)
    variance = float(p * (1.0 - p))
    return{
        "pmf": pmf,
        "mean":mean,
        "variance":variance
    }
    pass