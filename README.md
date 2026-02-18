# Option Pricing with the Black–Scholes Model

This project implements and explores the Black–Scholes option pricing framework in Python, using a SQL database as the only storage layer.

## Objectives

1. Implement Black–Scholes pricing for European call and put options.
2. Compute Greeks: $\Delta$, $\Gamma$, $\Theta$, $\nu$, $\rho$.
3. Compute implied volatility by numerical inversion of the model.
4. Use a SQL database for all data storage.
5. Build notebooks that derive theory, implement code, analyze results, and conclude the project.

## Mathematical Formulas

The call price is

$$
C = S_0 N(d_1) - K e^{-rT} N(d_2),
$$

and the put price is

$$
P = K e^{-rT} N(-d_2) - S_0 N(-d_1).
$$

with

$$
d_1 = \frac{\ln(S_0 / K) + (r + \sigma^2 / 2) T}{\sigma \sqrt{T}},
\qquad
d_2 = d_1 - \sigma \sqrt{T}.
$$

## Structure

- `option_pricing/` contains the implementation.
- `data/` contains the SQL database.
- `notebooks/` contains six notebooks:
  - **0** database setup  
  - **1** Black–Scholes fundamentals  
  - **2** implied volatility  
  - **3** Greeks  
  - **4** option strategies and P&L  
  - **5** conclusion (full markdown)

All code and markdown explanations are in English. All math uses `$...$` or `$$...$$`.
