"""Here we will visualise the energy levels and wavefunctions in a finite potential well. Solutions will be shown graphically and solved via sympy."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

class OneDFiniteSolutions:
    def __init__(self, v0):
        self.v0 = v0
        
r0 = 10

def solve(x):
    f1 = x[0]**2 + x[1]**2 - r0**2
    f2 = x[0] - x[1]*np.tan(x[1])
    return [f1, f2]

print(fsolve(solve, [11, 6]))
