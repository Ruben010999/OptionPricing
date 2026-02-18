import math


def _norm_cdf(x: float) -> float:
    """
    Standard normal cumulative distribution function N(x).
    """
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def black_scholes_call(S0: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Black–Scholes price of a European call option on a non-dividend-paying stock.
    """
    if T <= 0.0 or sigma <= 0.0:
        return max(S0 - K, 0.0)

    d1 = (math.log(S0 / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    return S0 * _norm_cdf(d1) - K * math.exp(-r * T) * _norm_cdf(d2)


def black_scholes_put(S0: float, K: float, T: float, r: float, sigma: float) -> float:
    """
    Black–Scholes price of a European put option on a non-dividend-paying stock.
    """
    if T <= 0.0 or sigma <= 0.0:
        return max(K - S0, 0.0)

    d1 = (math.log(S0 / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    return K * math.exp(-r * T) * _norm_cdf(-d2) - S0 * _norm_cdf(-d1)
