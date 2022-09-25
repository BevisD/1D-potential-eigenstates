# 1D-potential-eigenstates
Numerically Calculate the Eigenstates and Energies of a Bound Particle in any 1D Potential

## Introduction
The time-independent schrodinger equation, 
$\large\frac{-\hbar^2}{2m}\frac{\partial^2\psi(x)}{\partial x^2} + V(x)\psi(x) = E\psi(x)$ 
is only exactly solvable for a small number of conditions. The aim of this project is to create a tool that can solve the eigenfunctions $\psi_n(x)$ , and their corresponding energies $E_n$, for any potential function $V(x)$.

## Theory
The time-independent schrodinger equation can be put into discrete form. After setting $\hbar=1$ to set the units of the system, the resulting equation is obtained.
$$\large\frac{-1}{2m}\frac{\psi_{i+1}-2\psi_i+\psi_{i-1}}{(\Delta x)^2} + V(x)\psi_i = E\psi_i$$
This leads to a system of $N$ simultaneous equations. Setting the boundary conditions as $\psi(0) = 0, \psi(L) = 0$  (to force the states to be bound), we can represent this system as a $(N-1)*(N-1)$ matrix eigenvector equation.
