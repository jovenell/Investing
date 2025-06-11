import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# delta - sensitivity of option to change in price of the underlying
# gamma - rate of change of delta
# vega - sensitivity of option to change in volatility in the underlying
# theta - time decay
# rho - sensitivity of option to change in risk free rate

def main():
    while:
        try:
            S = float(input('Please enter the price: '))
            break
        except:
            pass
    K = float(input('Please enter the strike price: '))
    T = float(input('Please enter the time until expiration in years: '))
    R = float(input('Please enter the risk free rate: '))
    V = float(input('Please enter the volatility: '))
    put_or_call = input('Please enter C if the option is a call or P if the option is a put: ')

    N = norm.cdf

    print(calculate(S, K, T, R, V, N, put_or_call))

def calculate(S, K, T, R, V, N, put_or_call):
    D1 = d1(S, K, T, R, V)
    D2 = d2(T, V, D1)

    if put_or_call == 'C':
        visualize(K, T, R, V, put_or_call, D1, D2)
        return S * N(D1) - K * np.exp(-R * T) * N(D2)
    elif put_or_call == 'P':
        visualize(K, T, R, V, put_or_call, D1, D2)
        return K * np.exp(-R * T) * N(-D2) - S * N(-D1)

def d1(S, K, T, R, V):
    return (np.log(S / K) + (R + V ** 2 / 2) * T) / (V * np.sqrt(T)) 

def d2(T, V, D1):
    return D1 - V * np.sqrt(T)

def visualize(K, T, R, V, put_or_call, D1, D2):
    delta_vals, gamma_vals, theta_vals, vega_vals, rho_vals = [], [], [], [], []

    for S in np.linspace(50, 150, 100):
        delta, gamma, theta, vega, rho = greeks(S, K, T, R, V, put_or_call, D1, D2)
        delta_vals.append(delta)
        gamma_vals.append(gamma)
        theta_vals.append(theta)
        vega_vals.append(vega)
        rho_vals.append(rho)

    fig, axs = plt.subplots(3, 2, figsize=(12, 10))
    axs = axs.flatten()
    greek_names = ['Delta', 'Gamma', 'Theta', 'Vega', 'Rho']
    greek_vals = [delta_vals, gamma_vals, theta_vals, vega_vals, rho_vals]

    for i, greek in enumerate(greek_vals):
        axs[i].plot(np.linspace(50, 150, 100), greek)
        axs[i].set_title(f"{greek_names[i]} vs Stock Price")
        axs[i].set_xlabel("Stock Price (S)")
        axs[i].set_ylabel(greek_names[i])
        axs[i].grid(True)

    axs[-1].axis('off')

    plt.suptitle(f"Black-Scholes Greeks for a European {put_or_call.capitalize()} Option", fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

def greeks(S, K, T, R, V, put_or_call, D1, D2):
    if put_or_call == 'call':
        delta = norm.cdf(D1)
        theta = (-S * norm.pdf(D1) * V / (2 * np.sqrt(T)) - R * K * np.exp(-R * T) * norm.cdf(D2))
        rho = K * T * np.exp(-R * T) * norm.cdf(D2)
    else:
        delta = -norm.cdf(-D1)
        theta = (-S * norm.pdf(D1) * V / (2 * np.sqrt(T)) + R * K * np.exp(-R * T) * norm.cdf(-D2))
        rho = -K * T * np.exp(-R * T) * norm.cdf(-D2)

    gamma = norm.pdf(D1) / (S * V * np.sqrt(T))
    vega = S * norm.pdf(D1) * np.sqrt(T)

    return delta, gamma, theta, vega, rho

if __name__ == '__main__':
    main()
