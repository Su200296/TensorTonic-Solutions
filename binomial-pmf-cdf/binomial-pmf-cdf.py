import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    if k < 0:
        return {"pmf": 0.0, "cdf": 0.0}
    if k > n:
        return {"pmf": 0.0, "cdf": 1.0}

    pmf = float(math.comb(n, k) * (p ** k) * ((1.0 - p) ** (n - k)))
    cdf = float(sum(
        math.comb(n, i) * (p ** i) * ((1.0 - p) ** (n - i))
        for i in range(k + 1)
    ))

    return {
        "pmf": pmf,
        "cdf": cdf
    }