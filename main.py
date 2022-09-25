import numpy as np
from scipy.linalg import eigh_tridiagonal
import matplotlib.pyplot as plt

N = 200
X_RANGE = (-1, 1)

omega = 25


def potential(x):
    return 2 * omega ** 2 * x ** 2


def get_eigenstates(x, V):
    long_diag = V[1:-1] + 1 / (dx ** 2)
    short_diag = np.ones(N - 2) * -1 / (2 * dx ** 2)
    Es, states = eigh_tridiagonal(long_diag, short_diag)
    norm_states = states.transpose() / np.sqrt(dx)
    return Es, norm_states


x = np.linspace(X_RANGE[0], X_RANGE[1], N + 1)
V = potential(x)
dx = x[1] - x[0]

Es, states = get_eigenstates(x, V)


fig, axs = plt.subplots(1, 2, figsize=(12,6))
axs[0].set_title("$n_{th}$ Eigenstate in a\nQuadratic Potential")
for i in range(4):
    axs[0].plot(x[1:-1], states[i], label=f"$\psi_{i}$")
axs[0].legend()
axs[0].set(xlabel="$x$", ylabel="$\psi_n$")

axs[1].plot(Es[:60], label="Simulated $E_n$")
axs[1].plot(2 * (np.arange(0, 60) + 0.5) * omega, label=r"$(n+\frac{1}{2})\hbar\omega$")
axs[1].set_title("Energy of $n_{th}$ eigenstate")
axs[1].set(xlabel="$n$", ylabel="$E_n$")
axs[1].legend()
plt.show()
