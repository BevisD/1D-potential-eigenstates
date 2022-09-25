import numpy as np
import matplotlib.pyplot as plt
from eigensolver import get_eigenstates

# Number of discrete x values to calculate eigenstate
# The highest order of eigenstate is limited by N
N = 200
# Range of x values to simulate
# Potential is infinite outside of this range
X_RANGE = (-1, 1)
# Frequency of oscillation in the quadratic potential
# Scales how large the quadratic potential is
omega = 25


def potential(x):
    # Input x values as array
    # Output potential for each x value in array
    return 2 * omega ** 2 * x ** 2


def main():
    # Create x value array with N intervals (x is dimensionless)
    x = np.linspace(X_RANGE[0], X_RANGE[1], N + 1)
    V = potential(x)
    # Solve for energies and eigenstates
    Es, states = get_eigenstates(x, V)

    # Plot the first four eigenstates
    # Plot E_n against n for theory and simulated value to compare accuracy
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


if __name__ == '__main__':
    main()
