import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    x_mean = np.mean(x)
    x = np.asarray(x,dtype=float)
    z=[]
    for i in range(len(x)):
      z.append(i)
    std = np.sqrt(np.sum((x-x_mean)**2)/(len(x)-1))
    t = float((x_mean - mu0) / (std / np.sqrt(len(x))))

    return float(t)
    pass