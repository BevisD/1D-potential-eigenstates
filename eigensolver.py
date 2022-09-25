import numpy as np
from scipy.linalg import eigh_tridiagonal


def get_eigenstates(x, V):
    # Input x coordinates and corresponding potential values
    # Output energies and eigenstates
    # Eigenfunctions are output as a discrete array,
    # yet approximate true solutions for large N
    N = len(V)-1
    dx = x[1] - x[0]
    # The time independent schrodinger equation when discretized can be written
    # in Matrix form, this is a triadiagonal
    long_diag = V[1:-1] + 1 / (dx ** 2)
    short_diag = np.ones(N - 2) * -1 / (2 * dx ** 2)
    Es, states = eigh_tridiagonal(long_diag, short_diag)
    norm_states = states.transpose() / np.sqrt(dx)
    return Es, norm_states