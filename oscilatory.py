import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# 1. Definice systémů (přepis na soustavy 2 ODE)

def linear_oscillator(t, y, omega0, delta):
    """
    Lineární tlumený oscilátor: x'' + 2*delta*x' + omega0^2 * x = 0
    y = [x, v]
    """
    x, v = y
    dxdt = v
    dvdt = -2 * delta * v - (omega0**2) * x
    return [dxdt, dvdt]

def duffing_oscillator(t, y, delta, alpha, beta, gamma, omega):
    """
    Duffingův oscilátor: x'' + delta*x' + alpha*x + beta*x^3 = gamma*cos(omega*t)
    """
    x, v = y
    dxdt = v
    dvdt = -delta * v - alpha * x - beta * (x**3) + gamma * np.cos(omega * t)
    return [dxdt, dvdt]

def vanderpol_oscillator(t, y, mu):
    """
    Van der Polův oscilátor: x'' - mu*(1 - x^2)*x' + x = 0
    """
    x, v = y
    dxdt = v
    dvdt = mu * (1 - x**2) * v - x
    return [dxdt, dvdt]

# 2. Simulace a vykreslení

t_span = (0, 100)
t_eval = np.linspace(0, 100, 2000)
ics = [[1.0, 0.0], [0.1, 0.1], [2.5, -1.0]] # Různé počáteční podmínky

# --- VIZUALIZACE DUFFINGOVA OSCILÁTORU ---
delta, alpha, beta, gamma, omega = 0.2, -1.0, 1.0, 0.3, 1.2

plt.figure(figsize=(12, 5))
for ic in ics:
    sol = solve_ivp(duffing_oscillator, t_span, ic, args=(delta, alpha, beta, gamma, omega), t_eval=t_eval)
    plt.subplot(1, 2, 1)
    plt.plot(sol.t, sol.y[0], label=f"IC: {ic}")
    plt.subplot(1, 2, 2)
    plt.plot(sol.y[0], sol.y[1])

plt.subplot(1, 2, 1)
plt.title("Duffing: Časový průběh x(t)")
plt.xlabel("t"); plt.ylabel("x"); plt.legend()
plt.subplot(1, 2, 2)
plt.title("Duffing: Fázový diagram")
plt.xlabel("x"); plt.ylabel("v")
plt.tight_layout()
plt.show()

# --- POINCARÉHO PRŮŘEZ PRO DUFFINGA ---
# Vzorkování v čase t = n * T, kde T = 2*pi / omega
T = 2 * np.pi / omega
t_poincare = np.arange(0, 1000, T) # Delší čas pro lepší zobrazení atraktoru
sol_p = solve_ivp(duffing_oscillator, (0, 1000), [1.0, 0.0], args=(delta, alpha, beta, gamma, omega), t_eval=t_poincare)

plt.figure(figsize=(6, 5))
plt.scatter(sol_p.y[0], sol_p.y[1], s=5, color='red', alpha=0.6)
plt.title("Poincarého průřez (Duffing)")
plt.xlabel("x")
plt.ylabel("v")
plt.show()
