import time
import numpy as np
from numba import njit

def slow_sum(x):
    s = 0.0
    for i in range(len(x)):
        s += x[i] ** 2
    return s

@njit
def fast_sum(x):
    s = 0.0
    for i in range(len(x)):
        s += x[i] ** 2
    return s

def profile_demo(N=1000000):
    x = np.arange(N, dtype=np.float64)
    
    # Warm-up call to compile
    fast_sum(x)
    
    t0 = time.time()
    slow_sum(x)
    t1 = time.time()
    
    t2_start = time.time()
    fast_sum(x)  # now it's already compiled
    t2 = time.time()
    
    return {
        "slow": t1 - t0,
        "fast": t2 - t2_start,
        "speedup ratio": (t1 - t0) / (t2 - t2_start) #,
	#"diff": abs(s1 - s2)
    }

