"""Calculating the wavefunctions and probability functions for the 1D infinite potential well problem. Also calculates the probability functions for superposed states with time dependace."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class OneDInfiniteSolutions:
    """Takes a number n and calculates the wavefunction, probability function, and energy for an infinite square well. Solutions given are for a well with length 1."""
    def __init__(self, n):
        self.n = n
        self.h = 1.055*10**(-34) #reduced planks constant
        self.m = 9.11*10**(-31) #electron mass
        self.x_values = np.arange(0, 1, 0.001)
        self.tot_energy = self.energy(n)  
        self.y_p_values = self._probability_distribution()

    def __add__(self, other):
        """When addimg two wavefunctions together, we will generate a new object that handles the properties of superposed states"""
        return Superposition1DSolutions(self.n, other.n)

    def energy(self, n):
        """Calculates energy of an electron in a certain energy level"""
        return n**2 * np.pi**2 * (self.h**2) * 1/(2*self.m)

    def wavefunction(self, t):
        """Calculates real values for a wavefunction"""
        return np.sqrt(2) * np.sin(self.n * np.pi * self.x_values) * np.cos(t)

    def _probability_distribution(self):
        """Calculates probability distribution for electron"""
        return self.wavefunction(0) ** 2
 


class Superposition1DSolutions:
    """Takes a number n and m calculates the wavefunction and probability function for superposed wavefunction in an infinite square well. Solutions given are for a well with length 1. Limited to the addition of two wavefunctions"""
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.x_values = self.x_values = np.arange(0, 1, 0.001)

    def wavefunction(self, t):
        """Calculates real values superposed wavefunction"""
        return (np.sin(self.n * np.pi * self.x_values) + np.sin(self.m * np.pi * self.x_values)) * np.cos(t)

    def probability_distribution(self, t):
        """Calculates the probability distribution for the superposed wavefunctions"""
        return np.sin(self.n * np.pi * self.x_values)**2 + np.sin(self.m * np.pi * self.x_values)**2 + 2 * np.sin(self.n * np.pi * self.x_values) * np.sin(self.m * np.pi * self.x_values) * np.cos(t)


if __name__ == "__main__":
    a = OneDInfiniteSolutions(1)
    b = OneDInfiniteSolutions(3)
    c = a + b

    d = plt.figure()
    ax = plt.axes(xlim=(0, 1), ylim=(0, 5))
    line, = ax.plot([], [], lw=2)


    def f(t):
        line.set_data(c.x_values, c.probability_distribution(0.1*t))
        return line,


    anim = FuncAnimation(d, f, frames=1000, interval=20, blit=True)
    #plt.scatter(1, 1)
    plt.show()