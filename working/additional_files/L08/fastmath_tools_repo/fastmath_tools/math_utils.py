import math
import numpy as np

def gaussian(x, mu=0.0, sigma=1.0):
    return 1.0 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mu)/sigma)**2)

def integrate_simpson(f, a, b, N=1000):
    if N % 2 == 1:
        N += 1  # ensure even number of intervals
    x = np.linspace(a, b, N + 1)
    y = f(x)
    h = (b - a) / N
    return (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])
