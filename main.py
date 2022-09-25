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

fig = plt.figure(layout="constrained", figsize=(12, 6))
subfigs = fig.subfigures(1, 2)
axs0 = subfigs[0].subplots(4, 1, sharex=True)
axs1 = subfigs[1].subplots(1, 1)

subfigs[0].suptitle("$n_{th}$ Eigenstate in a\nQuadratic Potential")
subfigs[0].supxlabel("$x$")

for i in range(4):
    axs0[i].plot(x[1:-1], states[i], label=f"$\psi_{i}$")
    axs0[i].set(ylabel=f"$\psi_{i}$", ylim=(-2.5, 2.5))

axs1.plot(Es[:60], label="Simulated $E_n$")
axs1.plot(2 * (np.arange(0, 60) + 0.5) * omega, label=r"$(n+\frac{1}{2})\hbar\omega$")
axs1.set_title("Energy of $n_{th}$ eigenstate")
axs1.set(xlabel="$n$", ylabel="$E_n$")
axs1.legend()
plt.show()
