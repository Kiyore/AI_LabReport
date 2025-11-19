import random
import math

def cost_function(state):
    return sum(abs(state[i] - i) for i in range(len(state)))

def simulated_annealing_puzzle(puzzle):
    T = 1000
    alpha = 0.99
    Tmin = 0.1
    current_state = puzzle[:]
    random.shuffle(current_state)
    current_cost = cost_function(current_state)
    while T > Tmin:
        i, j = random.sample(range(len(current_state)), 2)
        new_state = current_state[:]
        new_state[i], new_state[j] = new_state[j], new_state[i]
        new_cost = cost_function(new_state)
        delta = new_cost - current_cost
        if delta < 0 or random.random() < math.exp(-delta / T):
            current_state = new_state
            current_cost = new_cost
        T *= alpha
    return current_state

puzzle = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(simulated_annealing_puzzle(puzzle))
