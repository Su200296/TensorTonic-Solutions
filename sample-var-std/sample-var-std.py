import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    arr = np.asarray(x, dtype=np.float64)
    n = len(arr)
    sam_var = float(np.sum((arr - np.mean(arr)) ** 2) / (n - 1))
    std_dev = float(np.sqrt(sam_var))

    return {
        "variance":sam_var,
        "standard_deviation":std_dev
    }
    pass