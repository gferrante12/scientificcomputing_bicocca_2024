import numpy as np
import random

def simulate_market(transition_matrix, states, N=10_000):
    """Simulate a Markov chain with given transition matrix."""
    state = random.choice(states)
    history = [state]
    for _ in range(N - 1):
        state = random.choices(states, weights=transition_matrix[states.index(state)])[0]
        history.append(state)
    return np.array(history)
