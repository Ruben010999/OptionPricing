### Delta of Call and Put vs Underlying Price

This plot shows how option delta changes with respect to the underlying price.
It highlights the nonlinear sensitivity of calls and puts and the role of moneyness.

![Delta vs Price](images/delta_vs_price.png)

---

### Volatility Arbitrage — Implied Volatility > Realized Volatility

When implied volatility is higher than realized volatility, 
a delta-hedged short straddle tends to generate positive P&L on average.

Histogram below shows the distribution of final P&L across many simulated paths.

![Volatility Arbitrage Positive](images/vol_arb_positive.png)

---

### Volatility Arbitrage — Implied Volatility < Realized Volatility

When implied volatility is lower than realized volatility,
the same delta-hedged short straddle tends to lose money on average.

This confirms the volatility risk premium intuition.

![Volatility Arbitrage Negative](images/vol_arb_negative.png)

# Option Pricing & Volatility Trading — Black–Scholes Project

A complete quantitative finance project implementing the Black–Scholes framework, option Greeks, delta hedging, and volatility trading simulations.

This project connects mathematical theory, numerical implementation, and trading intuition in a fully reproducible Python + SQL environment.

---

## Project Overview

This repository contains a full end-to-end implementation of:

- Black–Scholes option pricing
- Analytical Greeks
- Option payoff and strategy analysis
- Delta hedging engine
- Gamma scalping simulation
- Realized vs implied volatility comparison
- Volatility arbitrage Monte Carlo experiments

The project moves from static pricing formulas to dynamic hedging and P&L distribution analysis.

---

## Mathematical Foundation

Under the risk-neutral measure, the Black–Scholes price of a European call option is:

$$
C = S_0 N(d_1) - K e^{-rT} N(d_2)
$$

where

$$
d_1 = \frac{\ln(S_0/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma \sqrt{T}}
$$

$$
d_2 = d_1 - \sigma \sqrt{T}
$$

The project implements:

- Call and put pricing
- Greeks: $\Delta$, $\Gamma$, $\Theta$, $\nu$
- Implied volatility inversion
- Discrete delta hedging

---

## Database Layer (SQL)

All data is stored in a SQLite database.

Tables include:

- `assets`
- `asset_prices`
- `option_quotes`

The project uses SQL strictly for structured storage and retrieval.

---

## Key Experiments

### 1. Greeks & Sensitivity Analysis
- Analytical computation of $\Delta$, $\Gamma$, $\Theta$, $\nu$
- Sensitivity across price and volatility

### 2. Option Strategies
- Protective put
- Covered call
- Bull call spread
- Long straddle

Payoff and P&L diagrams at maturity.

### 3. Delta Hedging Engine
Discrete replication of:
- Long/short straddles
- Single call option

Demonstrates hedging error under discrete rebalancing.

### 4. Gamma Scalping
Shows that:

- If $\sigma_{real} > \sigma_{imp}$ → long gamma profits
- If $\sigma_{real} < \sigma_{imp}$ → long gamma loses

### 5. Volatility Arbitrage
Monte Carlo simulation of short straddles:

- Implied vol > realized vol → positive expected P&L
- Implied vol < realized vol → negative expected P&L

Demonstrates volatility as a tradable risk factor.

---

## Main Insight

This project shows that:

> Options are not directional bets — they are volatility instruments.

The relationship between realized and implied volatility determines long-run profitability of delta-hedged option strategies.

---

## Technologies Used

- Python
- NumPy
- Matplotlib
- SQLite (SQL)
- Jupyter Notebook

---

## Possible Extensions

- Stochastic volatility models (Heston)
- Jump diffusion models (Merton)
- Volatility surface calibration
- Transaction cost modeling
- Risk-neutral density extraction

---

## Author

Ruben Kostanyan  
Physics graduate | Quantitative Finance & Data Science

---

## License

MIT License
