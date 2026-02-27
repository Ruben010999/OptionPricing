<h2>Visual Results</h2>

<h3>Delta of Call and Put vs Underlying Price</h3>

<p>
This plot shows how option delta changes with respect to the underlying price.
It highlights the nonlinear sensitivity of calls and puts and the role of moneyness.
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/Ruben010999/OptionPricing/main/images/delta_vs_price.png" width="700">
</p>

<hr>

<h3>Volatility Arbitrage — Implied Volatility &gt; Realized Volatility</h3>

<p>
When implied volatility is higher than realized volatility, 
a delta-hedged short straddle tends to generate positive P&amp;L on average.
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/Ruben010999/OptionPricing/main/images/vol_arb_positive.png" width="700">
</p>

<hr>

<h3>Volatility Arbitrage — Implied Volatility &lt; Realized Volatility</h3>

<p>
When implied volatility is lower than realized volatility,
the same delta-hedged short straddle tends to lose money on average.
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/Ruben010999/OptionPricing/main/images/vol_arb_negative.png" width="700">
</p>


# Option Pricing & Volatility Trading — Black–Scholes + Machine Learning Project

A complete quantitative finance project implementing:

- The Black–Scholes analytical framework  
- Greeks and dynamic hedging  
- Volatility arbitrage simulations  
- Machine learning volatility forecasting  
- Empirical strategy evaluation  

This repository connects mathematical derivatives theory, numerical simulation, database engineering, and data-driven modeling in a fully reproducible Python + SQL environment.

---

## Project Overview

This project develops a coherent quantitative architecture progressing through four layers:

1. **Analytical pricing (Black–Scholes)**
2. **Risk decomposition (Greeks & hedging)**
3. **Volatility arbitrage via simulation**
4. **Machine learning volatility forecasting & strategy integration**

The objective is not only to implement formulas, but to connect:

- Theory  
- Simulation  
- Statistical modeling  
- Economic interpretation  

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

This forms the structural backbone of the framework.

---

## Database Layer (SQL)

All market data is stored in a SQLite database.

Tables include:

- `assets`
- `asset_prices`
- `option_quotes`

SQL is used strictly for structured storage and retrieval, separating data management from modeling logic.

---

## Core Modules

### 1. Greeks & Sensitivity Analysis

- Analytical computation of $\Delta$, $\Gamma$, $\Theta$, $\nu$
- Sensitivity analysis across price and volatility

Local risk decomposition:

$$
dV \approx \Delta dS + \frac{1}{2}\Gamma dS^2 + \Theta dt
$$

---

### 2. Option Strategies

- Protective put  
- Covered call  
- Bull call spread  
- Long straddle  

Includes payoff diagrams and P&L analysis at maturity.

---

### 3. Delta Hedging Engine

Discrete replication of:

- Long/short straddles  
- Single call options  

Demonstrates:

- Replication error under discrete rebalancing  
- Sensitivity to realized volatility  
- Gamma-driven P&L dynamics  

---

### 4. Gamma Scalping & Volatility Arbitrage

Monte Carlo simulations confirm:

- If $\sigma_{real} > \sigma_{imp}$ → long gamma profits  
- If $\sigma_{real} < \sigma_{imp}$ → long gamma loses  

Expected P&L approximately follows:

$$
\mathbb{E}[\text{P\&L}] \propto \sigma_{imp}^2 - \sigma_{real}^2
$$

This demonstrates volatility as a tradable relative-value risk factor.

---

## 5. Machine Learning Volatility Forecasting

The project extends beyond theoretical volatility comparison into empirical forecasting.

### Feature Engineering

Constructed rolling realized volatility features:

- 5-day volatility  
- 10-day volatility  
- 20-day volatility  

Target:

- Next-period realized volatility (shifted forward to prevent leakage)

Time-series split: 80% train / 20% validation.

### Model

- XGBoost Regressor  
- Out-of-sample evaluation  

### Results

- Validation RMSE ≈ **0.00046**
- Residual mean ≈ 0 (no strong bias)
- Stable performance across volatility regimes
- Captures volatility clustering effectively
- Performance weakens during abrupt regime shifts

---

## Strategy Integration

Volatility forecasts were integrated into a simple trading rule:

- Long exposure when predicted volatility > median  
- Short exposure otherwise  

Out-of-sample results:

- Strategy cumulative return ≈ **1.018**
- Passive benchmark return ≈ **1.122**

The strategy underperformed the benchmark.

---

## Key Insights

This project establishes two major conclusions:

1. **Volatility mispricing drives theoretical option profitability.**
2. **Statistical forecast accuracy does not guarantee economic alpha.**

Even with statistically sound volatility forecasts:

- Signal transformation matters.
- Market efficiency compresses simple predictive edges.
- Monetizing small volatility improvements is structurally difficult.

This bridges classical derivatives theory with modern machine learning reality.

---

## Technologies Used

- Python  
- NumPy  
- Matplotlib  
- XGBoost  
- SQLite (SQL)  
- Jupyter Notebook  

---

## Research Extensions

Future directions include:

- Walk-forward validation  
- SHAP interpretability analysis  
- Stochastic volatility models (Heston)  
- Jump diffusion (Merton)  
- Volatility surface calibration  
- Transaction cost modeling  
- Quantile regression for tail risk  

---

## Author

Ruben Kostanyan  
Physics Graduate  
Quantitative Finance & Data Science  

Focused on derivatives modeling, volatility research, and systematic strategy design.

---

## License

MIT License
