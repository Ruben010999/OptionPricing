import math
from .black_scholes import _norm_cdf


def _norm_pdf(x: float) -> float:
    """Standard normal probability density function."""
    return math.exp(-0.5 * x * x) / math.sqrt(2 * math.pi)


def d1(S0, K, T, r, sigma):
    return (math.log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))


def d2(S0, K, T, r, sigma):
    return d1(S0, K, T, r, sigma) - sigma * math.sqrt(T)


def delta_call(S0, K, T, r, sigma):
    return _norm_cdf(d1(S0, K, T, r, sigma))


def delta_put(S0, K, T, r, sigma):
    return _norm_cdf(d1(S0, K, T, r, sigma)) - 1.0


def gamma(S0, K, T, r, sigma):
    return _norm_pdf(d1(S0, K, T, r, sigma)) / (S0 * sigma * math.sqrt(T))


def vega(S0, K, T, r, sigma):
    return S0 * _norm_pdf(d1(S0, K, T, r, sigma)) * math.sqrt(T)


def theta_call(S0, K, T, r, sigma):
    d_1 = d1(S0, K, T, r, sigma)
    d_2 = d_1 - sigma * math.sqrt(T)
    term1 = -(S0 * _norm_pdf(d_1) * sigma) / (2 * math.sqrt(T))
    term2 = -r * K * math.exp(-r * T) * _norm_cdf(d_2)
    return term1 + term2


def theta_put(S0, K, T, r, sigma):
    d_1 = d1(S0, K, T, r, sigma)
    d_2 = d_1 - sigma * math.sqrt(T)
    term1 = -(S0 * _norm_pdf(d_1) * sigma) / (2 * math.sqrt(T))
    term2 = r * K * math.exp(-r * T) * _norm_cdf(-d_2)
    return term1 + term2


def rho_call(S0, K, T, r, sigma):
    return K * T * math.exp(-r * T) * _norm_cdf(d2(S0, K, T, r, sigma))


def rho_put(S0, K, T, r, sigma):
    return -K * T * math.exp(-r * T) * _norm_cdf(-d2(S0, K, T, r, sigma))
