1. Black-Scholes Option Pricing Model
Goal: Learn how options are priced using closed-form solutions.
What to Build:
Implement the Black-Scholes formula for European call/put options.
Plot option price vs. strike price, time to maturity, volatility.
Tools: Python, SciPy, Matplotlib
Extension: Add calculation and visualization of Greeks (Delta, Gamma, Vega, etc.)

2. Binomial Tree Option Pricing
Goal: Understand discrete-time option pricing.
What to Build:
A binomial tree model for American and European options.
Visualize the tree and option value at each node.
Tools: Python, networkx or graphviz for tree visualization
Extension: Compare results with Black-Scholes for validation.

3. Monte Carlo Simulation for Option Pricing
Goal: Learn stochastic simulation techniques.
What to Build:
Simulate asset price paths using geometric Brownian motion.
Estimate option prices using Monte Carlo.
Tools: Python, NumPy, Matplotlib
Extension: Add variance reduction techniques (e.g., antithetic variates).

4. Backtest a Simple Trading Strategy
Goal: Understand strategy evaluation.
What to Build:
A moving average crossover strategy.
Backtest with performance metrics: Sharpe ratio, drawdown, CAGR.
Tools: Backtrader, Zipline, or custom Python code
Extension: Add transaction costs and slippage modeling.

5. Portfolio Optimization
Goal: Learn modern portfolio theory.
What to Build:
Mean-variance optimization using historical returns.
Visualize the efficient frontier and optimal portfolios.
Tools: cvxpy, Pandas, Matplotlib
Extension: Add constraints (e.g., no shorting, sector limits).